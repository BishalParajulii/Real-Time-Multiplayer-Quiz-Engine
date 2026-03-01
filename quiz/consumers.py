import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from django.db.models import Sum

from .models import Option, PlayerAnswer, Question, Quiz
from .tasks import close_question_task


class QuizConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_code = self.scope["url_route"]["kwargs"]["room_code"].upper()
        self.room_group_name = f"quiz_{self.room_code}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get("type")

        if event_type == "start_quiz":
            await self.start_quiz()
        elif event_type == "submit_answer":
            await self.submit_answer(data)

    async def start_quiz(self):
        try:
            quiz = await sync_to_async(Quiz.objects.get)(room_code=self.room_code)
        except Quiz.DoesNotExist:
            await self.send_error("Quiz not found.")
            return

        question = await sync_to_async(quiz.questions.first)()

        if question is None:
            await self.send_error("No questions are available in this quiz.")
            return

        options = await sync_to_async(list)(question.options.all())

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_question",
                "question_id": question.id,
                "text": question.text,
                "timer": question.timer_seconds,
                "options": [{"id": opt.id, "text": opt.text} for opt in options],
            },
        )

        close_question_task.apply_async(
            (self.room_code, question.id),
            countdown=question.timer_seconds,
        )

    async def send_question(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "question",
                    "question_id": event["question_id"],
                    "text": event["text"],
                    "timer": event["timer"],
                    "options": event["options"],
                }
            )
        )

    async def submit_answer(self, data):
        user_id = data.get("user_id")
        question_id = data.get("question_id")
        option_id = data.get("option_id")

        try:
            user = await sync_to_async(User.objects.get)(id=user_id)
            question = await sync_to_async(Question.objects.select_related("quiz").get)(id=question_id)
            option = await sync_to_async(Option.objects.get)(id=option_id, question=question)
        except (User.DoesNotExist, Question.DoesNotExist, Option.DoesNotExist):
            await self.send_error("Invalid answer submission payload.")
            return

        if question.quiz.room_code != self.room_code:
            await self.send_error("This question does not belong to the current room.")
            return

        answer_exists = await sync_to_async(
            PlayerAnswer.objects.filter(player=user, question=question).exists
        )()
        if answer_exists:
            await self.send_error("You already submitted an answer for this question.")
            return

        score = 10 if option.is_correct else 0

        await sync_to_async(PlayerAnswer.objects.create)(
            player=user,
            question=question,
            selected_option=option,
            score=score,
        )

        await self.update_leaderboard()

    async def update_leaderboard(self):
        leaderboard = await sync_to_async(
            lambda: list(
                PlayerAnswer.objects.filter(question__quiz__room_code=self.room_code)
                .values("player__username")
                .annotate(total_score=Sum("score"))
                .order_by("-total_score", "player__username")
            )
        )()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "leaderboard",
                "leaderboard": leaderboard,
            },
        )

    async def leaderboard(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "leaderboard",
                    "data": event["leaderboard"],
                }
            )
        )

    async def question_closed(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "question_closed",
                    "question_id": event["question_id"],
                }
            )
        )

    async def quiz_finished(self, event):
        await self.send(text_data=json.dumps({"type": "quiz_finished"}))

    async def send_error(self, message):
        await self.send(text_data=json.dumps({"type": "error", "message": message}))
