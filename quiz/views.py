from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Option, Question, Quiz
from .question_bank import generate_nepal_questions
from .serializers import QuizSerializer

QUIZ_CATEGORIES = {
    "math": {"name": "Maths", "amount": 100},
    "computer": {"name": "Computer", "amount": 100},
    "history": {"name": "History", "amount": 100},
    "geography": {"name": "Geography", "amount": 100},
    "mythology": {"name": "Mythology", "amount": 100},
    "gk": {"name": "General Knowledge", "amount": 100},
}


def _system_user():
    user, _ = User.objects.get_or_create(username="quizbot")
    return user


def _quiz_category_key(quiz):
    title = (quiz.title or "").strip()
    if title.startswith("[") and "]" in title:
        key = title.split("]", 1)[0].replace("[", "").strip().lower()
        if key in QUIZ_CATEGORIES:
            return key
    return "gk"


def _ensure_questions_for_quiz(quiz, category_key, timer_seconds=15):
    config = QUIZ_CATEGORIES.get(category_key, QUIZ_CATEGORIES["gk"])
    target_count = config["amount"]
    existing_count = quiz.questions.count()
    if existing_count >= target_count:
        return {"created_questions": 0, "source": "existing"}

    needed = target_count - existing_count
    rows = generate_nepal_questions(category_key=category_key, count=target_count)
    existing_texts = set(quiz.questions.values_list("text", flat=True))

    created_questions = 0
    with transaction.atomic():
        for row in rows:
            if row["text"] in existing_texts:
                continue
            question = Question.objects.create(
                quiz=quiz,
                text=row["text"],
                timer_seconds=timer_seconds,
            )
            created_questions += 1
            existing_texts.add(row["text"])

            for option in row["options"]:
                Option.objects.create(
                    question=question,
                    text=option["text"][:200],
                    is_correct=option["is_correct"],
                )

            if created_questions >= needed:
                break

    return {"created_questions": created_questions, "source": "local_bank"}


class CategoryListView(APIView):
    def get(self, request):
        categories = []
        for key, config in QUIZ_CATEGORIES.items():
            categories.append(
                {
                    "key": key,
                    "name": config["name"],
                    "amount": config["amount"],
                    "source": "local_nepal_bank",
                }
            )
        return Response({"categories": categories}, status=status.HTTP_200_OK)


class QuizCreateView(APIView):
    def post(self, request):
        title = (request.data.get("title") or "").strip()
        if not title:
            return Response({"error": "title is required"}, status=status.HTTP_400_BAD_REQUEST)

        quiz = Quiz.objects.create(title=title, host=_system_user())
        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class JoinQuizView(APIView):
    def post(self, request):
        username = (request.data.get("username") or "").strip()
        room_code = (request.data.get("room_code") or "").strip().upper()
        category = (request.data.get("category") or "").strip().lower()

        if not username:
            return Response({"error": "username is required"}, status=status.HTTP_400_BAD_REQUEST)

        if room_code:
            try:
                quiz = Quiz.objects.get(room_code=room_code)
            except Quiz.DoesNotExist:
                return Response({"error": "Quiz room not found"}, status=status.HTTP_404_NOT_FOUND)
            category_key = _quiz_category_key(quiz)
        else:
            if category not in QUIZ_CATEGORIES:
                return Response(
                    {"error": "Valid category is required when room_code is not provided"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            category_key = category
            category_name = QUIZ_CATEGORIES[category_key]["name"]
            quiz = Quiz.objects.create(
                title=f"[{category_key}] {category_name} Quiz",
                host=_system_user(),
            )

        player, _ = User.objects.get_or_create(username=username)
        created_info = _ensure_questions_for_quiz(quiz, category_key=category_key)

        serializer = QuizSerializer(quiz)
        response = serializer.data
        response["player_id"] = player.id
        response["category"] = category_key
        response["category_name"] = QUIZ_CATEGORIES.get(category_key, QUIZ_CATEGORIES["gk"])["name"]
        response["created_questions"] = created_info["created_questions"]
        response["question_source"] = created_info["source"]
        return Response(response, status=status.HTTP_200_OK)


class BulkQuestionCreateView(APIView):
    def post(self, request):
        room_code = (request.data.get("room_code") or "").strip().upper()
        questions = request.data.get("questions") or []

        if not room_code:
            return Response(
                {"error": "room_code is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not isinstance(questions, list) or not questions:
            return Response(
                {"error": "questions must be a non-empty list"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            quiz = Quiz.objects.get(room_code=room_code)
        except Quiz.DoesNotExist:
            return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

        created_questions = 0
        created_options = 0
        errors = []

        with transaction.atomic():
            for idx, question_data in enumerate(questions, start=1):
                if not isinstance(question_data, dict):
                    errors.append(f"questions[{idx}] must be an object")
                    continue

                text = (question_data.get("text") or "").strip()
                timer_seconds = question_data.get("timer_seconds", 15)
                options = question_data.get("options")

                if not text:
                    errors.append(f"questions[{idx}].text is required")
                    continue

                try:
                    timer_seconds = int(timer_seconds)
                except (TypeError, ValueError):
                    errors.append(f"questions[{idx}].timer_seconds must be an integer")
                    continue

                if timer_seconds <= 0:
                    errors.append(f"questions[{idx}].timer_seconds must be > 0")
                    continue

                if not isinstance(options, list) or len(options) < 2:
                    errors.append(f"questions[{idx}].options must have at least 2 options")
                    continue

                valid_options = []
                correct_count = 0
                for opt_idx, opt in enumerate(options, start=1):
                    if not isinstance(opt, dict):
                        errors.append(f"questions[{idx}].options[{opt_idx}] must be an object")
                        valid_options = []
                        break

                    opt_text = (opt.get("text") or "").strip()
                    is_correct = bool(opt.get("is_correct", False))
                    if not opt_text:
                        errors.append(f"questions[{idx}].options[{opt_idx}].text is required")
                        valid_options = []
                        break

                    if is_correct:
                        correct_count += 1
                    valid_options.append((opt_text, is_correct))

                if not valid_options:
                    continue

                if correct_count == 0:
                    errors.append(f"questions[{idx}] must include at least one correct option")
                    continue

                question = Question.objects.create(
                    quiz=quiz,
                    text=text,
                    timer_seconds=timer_seconds,
                )
                created_questions += 1

                for opt_text, is_correct in valid_options:
                    Option.objects.create(
                        question=question,
                        text=opt_text,
                        is_correct=is_correct,
                    )
                    created_options += 1

        response_payload = {
            "room_code": quiz.room_code,
            "created_questions": created_questions,
            "created_options": created_options,
            "total_questions_in_quiz": quiz.questions.count(),
        }

        if errors:
            response_payload["errors"] = errors
            return Response(response_payload, status=status.HTTP_207_MULTI_STATUS)

        return Response(response_payload, status=status.HTTP_201_CREATED)


class OpenTDBImportView(APIView):
    def post(self, request):
        return Response(
            {"error": "OpenTDB import disabled. Using local Nepal question bank."},
            status=status.HTTP_410_GONE,
        )


def index(request):
    return render(request, "quiz/index.html")


def create_room(request):
    return render(request, "quiz/create_room.html")


def room(request, room_code):
    return render(
        request,
        "quiz/room.html",
        {
            "room_code": room_code,
        },
    )
