import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Quiz, Question, Option, PlayerAnswer
from asgiref.sync import sync_to_async
from .tasks import close_question_task

class QuizConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_code = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = f'quiz_{self.room_code}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get("type")

        if event_type == "start_quiz":
            await self.start_quiz()

        elif event_type == "submit_answer":
            await self.submit_answer(data)

    # ----------------------------
    # Start Quiz (Host triggers)
    # ----------------------------
    async def start_quiz(self):
        quiz = await sync_to_async(Quiz.objects.get)(room_code=self.room_code)
        question = await sync_to_async(quiz.questions.first)()

        options = await sync_to_async(list)(question.options.all())

        # Broadcast question
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_question",
                "question_id": question.id,
                "text": question.text,
                "timer": question.timer_seconds,
                "options": [
                    {"id": opt.id, "text": opt.text}
                    for opt in options
                ]
            }
        )

        # Schedule closing task
        close_question_task.apply_async(
            (self.room_code, question.id),
            countdown=question.timer_seconds
        )
    # ----------------------------
    # Broadcast Question
    # ----------------------------
    async def send_question(self, event):
        await self.send(text_data=json.dumps({
            "type": "question",
            "question_id": event["question_id"],
            "text": event["text"],
            "timer": event["timer"],
            "options": event["options"]
        }))

    # ----------------------------
    # Handle Answer Submission
    # ----------------------------
    async def submit_answer(self, data):
        user_id = data.get("user_id")
        question_id = data.get("question_id")
        option_id = data.get("option_id")

        user = await sync_to_async(User.objects.get)(id=user_id)
        question = await sync_to_async(Question.objects.get)(id=question_id)
        option = await sync_to_async(Option.objects.get)(id=option_id)

        score = 0
        if option.is_correct:
            score = 10  # basic scoring

        await sync_to_async(PlayerAnswer.objects.create)(
            player=user,
            question=question,
            selected_option=option,
            score=score
        )

        await self.update_leaderboard()

    # ----------------------------
    # Leaderboard Update
    # ----------------------------
    async def update_leaderboard(self):
        from django.db.models import Sum

        leaderboard = await sync_to_async(
            lambda: list(
                PlayerAnswer.objects.values("player__username")
                .annotate(total_score=Sum("score"))
                .order_by("-total_score")
            )
        )()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "leaderboard",
                "leaderboard": leaderboard
            }
        )

    async def leaderboard(self, event):
        await self.send(text_data=json.dumps({
            "type": "leaderboard",
            "data": event["leaderboard"]
        }))