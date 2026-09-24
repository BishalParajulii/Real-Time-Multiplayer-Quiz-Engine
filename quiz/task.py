import random

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

from .models import Quiz


DIFFICULTY_ORDER = {"easy": 0, "medium": 1, "hard": 2}


def get_questions_in_play_order(quiz):
    # Room-seeded shuffle so every player in the room sees the same order,
    # but different rooms get a different (randomized) question sequence.
    questions = list(quiz.questions.all())
    rng = random.Random(quiz.room_code)
    rng.shuffle(questions)

    easy = [q for q in questions if q.difficulty == "easy"]
    medium = [q for q in questions if q.difficulty == "medium"]
    hard = [q for q in questions if q.difficulty == "hard"]
    other = [q for q in questions if q.difficulty not in DIFFICULTY_ORDER]

    # Guarantee the first 10 are easy, then ramp gradually:
    # interleave remaining easy with medium, and save hard for later.
    opening_easy = easy[:10]
    rng.shuffle(opening_easy)

    ramp = []
    rest_easy = easy[10:]
    i = j = 0
    while i < len(rest_easy) or j < len(medium):
        if i < len(rest_easy) and (j >= len(medium) or i <= j):
            ramp.append(rest_easy[i])
            i += 1
        elif j < len(medium):
            ramp.append(medium[j])
            j += 1

    ordered = opening_easy
    ordered += ramp
    ordered += hard
    ordered += other
    return ordered


@shared_task
def close_question_task(room_code, question_id):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        f"quiz_{room_code}",
        {
            "type": "question_closed",
            "question_id": question_id,
        },
    )

    quiz = Quiz.objects.get(room_code=room_code)
    questions = get_questions_in_play_order(quiz)

    for index, q in enumerate(questions):
        if q.id == question_id and index + 1 < len(questions):
            next_q = questions[index + 1]

            async_to_sync(channel_layer.group_send)(
                f"quiz_{room_code}",
                {
                    "type": "send_question",
                    "question_id": next_q.id,
                    "text": next_q.text,
                    "timer": next_q.timer_seconds,
                    "options": [
                        {"id": opt.id, "text": opt.text}
                        for opt in next_q.options.all()
                    ],
                },
            )

            close_question_task.apply_async(
                (room_code, next_q.id),
                countdown=next_q.timer_seconds,
            )
            return

    async_to_sync(channel_layer.group_send)(
        f"quiz_{room_code}",
        {
            "type": "quiz_finished",
        },
    )
