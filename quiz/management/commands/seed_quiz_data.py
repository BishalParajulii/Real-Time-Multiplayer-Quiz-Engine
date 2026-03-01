import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from quiz.models import Option, Question, Quiz


def _make_math_question(index):
    a = (index * 3) % 47 + 2
    b = (index * 5) % 31 + 1
    op = ["+", "-", "*"][index % 3]

    if op == "+":
        answer = a + b
        text = f"What is {a} + {b}?"
    elif op == "-":
        answer = a - b
        text = f"What is {a} - {b}?"
    else:
        answer = a * b
        text = f"What is {a} × {b}?"

    wrong = {answer + 1, answer - 1, answer + 2, answer - 2, answer + 3}
    wrong.discard(answer)
    wrong_choices = list(wrong)[:3]

    options = [str(answer)] + [str(x) for x in wrong_choices]
    random.shuffle(options)
    return text, str(answer), options


def _make_gk_question(index):
    items = [
        ("Which planet is known as the Red Planet?", "Mars", ["Venus", "Jupiter", "Saturn"]),
        ("How many days are there in a leap year?", "366", ["365", "364", "360"]),
        ("What is the largest ocean on Earth?", "Pacific Ocean", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]),
        ("What is H2O commonly known as?", "Water", ["Hydrogen", "Salt", "Oxygen"]),
        ("What color do you get by mixing blue and yellow?", "Green", ["Red", "Purple", "Orange"]),
        ("Which gas do plants absorb from the atmosphere?", "Carbon dioxide", ["Oxygen", "Nitrogen", "Helium"]),
        ("How many continents are there on Earth?", "7", ["5", "6", "8"]),
        ("Which language is primarily used with Django?", "Python", ["Java", "PHP", "C#"]),
        ("What is the capital of Japan?", "Tokyo", ["Kyoto", "Osaka", "Nagoya"]),
        ("Which device routes network traffic between computers?", "Router", ["Monitor", "Keyboard", "Printer"]),
    ]

    text, answer, distractors = items[index % len(items)]
    options = [answer] + distractors
    random.shuffle(options)
    return text, answer, options


class Command(BaseCommand):
    help = "Seed a quiz with test questions and options."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=50, help="Number of questions to create (default: 50)")
        parser.add_argument("--username", type=str, default="host", help="Host username (default: host)")
        parser.add_argument("--title", type=str, default="Demo Quiz", help="Quiz title (default: Demo Quiz)")
        parser.add_argument("--room-code", type=str, default="", help="Existing room code to add questions to")
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete existing questions/options for target quiz before seeding",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        count = max(1, options["count"])
        username = options["username"].strip() or "host"
        title = options["title"].strip() or "Demo Quiz"
        room_code = (options["room_code"] or "").strip().upper()
        should_reset = options["reset"]

        host, _ = User.objects.get_or_create(username=username)

        if room_code:
            quiz = Quiz.objects.filter(room_code=room_code).first()
            if quiz is None:
                quiz = Quiz.objects.create(title=title, host=host, room_code=room_code)
                self.stdout.write(self.style.SUCCESS(f"Created quiz room: {quiz.room_code}"))
            else:
                self.stdout.write(self.style.WARNING(f"Using existing quiz room: {quiz.room_code}"))
        else:
            quiz = Quiz.objects.create(title=title, host=host)
            self.stdout.write(self.style.SUCCESS(f"Created new quiz room: {quiz.room_code}"))

        if should_reset:
            Question.objects.filter(quiz=quiz).delete()
            self.stdout.write(self.style.WARNING("Deleted existing questions for this quiz."))

        created_questions = 0
        for i in range(count):
            if i % 2 == 0:
                text, answer, option_values = _make_math_question(i)
            else:
                text, answer, option_values = _make_gk_question(i)

            question = Question.objects.create(
                quiz=quiz,
                text=f"Q{i + 1}. {text}",
                timer_seconds=15,
            )

            for value in option_values[:4]:
                Option.objects.create(
                    question=question,
                    text=value,
                    is_correct=(value == answer),
                )

            created_questions += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete: {created_questions} questions added to room {quiz.room_code}."
            )
        )
        self.stdout.write(
            f"Host username: {host.username} | Quiz title: {quiz.title} | Room code: {quiz.room_code}"
        )
