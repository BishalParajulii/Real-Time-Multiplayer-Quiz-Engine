from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

from .models import Quiz


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
    questions = list(quiz.questions.all())

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
