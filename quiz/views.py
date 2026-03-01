import base64
import html
import json
import random
from urllib import parse, request as urllib_request
from urllib.error import URLError

from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Option, Question, Quiz
from .serializers import QuizSerializer

QUIZ_CATEGORIES = {
    "math": {
        "name": "Maths",
        "amount": 20,
        "category": 19,
        "difficulty": "hard",
        "type": "multiple",
    },
    "computer": {
        "name": "Computer",
        "amount": 20,
        "category": 18,
        "difficulty": "hard",
        "type": "multiple",
    },
    "history": {
        "name": "History",
        "amount": 20,
        "category": 23,
        "difficulty": "hard",
        "type": "multiple",
    },
    "geography": {
        "name": "Geography",
        "amount": 20,
        "category": 22,
        "difficulty": "hard",
        "type": "multiple",
    },
    "mythology": {
        "name": "Mythology",
        "amount": 20,
        "category": 20,
        "difficulty": "hard",
        "type": "multiple",
    },
    "gk": {
        "name": "General Knowledge",
        "amount": 20,
        "category": 9,
        "difficulty": "hard",
        "type": "multiple",
    },
}


def _system_user():
    user, _ = User.objects.get_or_create(username="quizbot")
    return user


def _decode_b64(text):
    return html.unescape(base64.b64decode(text).decode("utf-8")).strip()


def _build_opentdb_url(amount, category, difficulty, question_type):
    params = parse.urlencode(
        {
            "amount": amount,
            "category": category,
            "difficulty": difficulty,
            "type": question_type,
            "encode": "base64",
        }
    )
    return f"https://opentdb.com/api.php?{params}"


def _fetch_opentdb_questions(amount, category, difficulty, question_type):
    api_url = _build_opentdb_url(amount, category, difficulty, question_type)
    with urllib_request.urlopen(api_url, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))

    if payload.get("response_code") != 0:
        return []

    rows = []
    for item in payload.get("results", []):
        text = _decode_b64(item.get("question", ""))
        correct_answer = _decode_b64(item.get("correct_answer", ""))
        incorrect_answers = [_decode_b64(answer) for answer in item.get("incorrect_answers", [])]

        if not text or not correct_answer:
            continue

        options = [{"text": correct_answer, "is_correct": True}]
        options.extend(
            {"text": answer, "is_correct": False}
            for answer in incorrect_answers
            if answer
        )
        random.shuffle(options)

        if len(options) < 2:
            continue

        rows.append(
            {
                "text": text,
                "options": options,
            }
        )
    return rows


def _quiz_category_key(quiz):
    title = (quiz.title or "").strip()
    if title.startswith("[") and "]" in title:
        key = title.split("]", 1)[0].replace("[", "").strip().lower()
        if key in QUIZ_CATEGORIES:
            return key
    return "gk"


def _ensure_questions_for_quiz(quiz, category_key, timer_seconds=15):
    if quiz.questions.exists():
        return 0

    config = QUIZ_CATEGORIES.get(category_key, QUIZ_CATEGORIES["gk"])
    rows = _fetch_opentdb_questions(
        amount=config["amount"],
        category=config["category"],
        difficulty=config["difficulty"],
        question_type=config["type"],
    )

    created_questions = 0
    with transaction.atomic():
        for row in rows:
            question = Question.objects.create(
                quiz=quiz,
                text=row["text"],
                timer_seconds=timer_seconds,
            )
            created_questions += 1

            for option in row["options"]:
                Option.objects.create(
                    question=question,
                    text=option["text"][:200],
                    is_correct=option["is_correct"],
                )

    return created_questions


class CategoryListView(APIView):
    def get(self, request):
        categories = []
        for key, config in QUIZ_CATEGORIES.items():
            categories.append(
                {
                    "key": key,
                    "name": config["name"],
                    "amount": config["amount"],
                    "difficulty": config["difficulty"],
                    "type": config["type"],
                    "category_id": config["category"],
                    "source_url": _build_opentdb_url(
                        amount=config["amount"],
                        category=config["category"],
                        difficulty=config["difficulty"],
                        question_type=config["type"],
                    ),
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

        try:
            created = _ensure_questions_for_quiz(quiz, category_key=category_key)
        except URLError:
            return Response(
                {"error": "Could not load questions from OpenTDB right now"},
                status=status.HTTP_502_BAD_GATEWAY,
            )
        except json.JSONDecodeError:
            return Response(
                {"error": "Invalid response from OpenTDB"},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        serializer = QuizSerializer(quiz)
        response = serializer.data
        response["player_id"] = player.id
        response["category"] = category_key
        response["category_name"] = QUIZ_CATEGORIES.get(category_key, QUIZ_CATEGORIES["gk"])["name"]
        response["created_questions"] = created
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
        room_code = (request.data.get("room_code") or "").strip().upper()

        amount = request.data.get("amount", 10)
        category = request.data.get("category", 19)
        difficulty = (request.data.get("difficulty") or "hard").strip().lower()
        question_type = (request.data.get("type") or "multiple").strip().lower()
        timer_seconds = request.data.get("timer_seconds", 15)

        if not room_code:
            return Response(
                {"error": "room_code is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            amount = int(amount)
            category = int(category)
            timer_seconds = int(timer_seconds)
        except (TypeError, ValueError):
            return Response(
                {"error": "amount, category and timer_seconds must be integers"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if amount <= 0 or amount > 50:
            return Response(
                {"error": "amount must be between 1 and 50"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if timer_seconds <= 0:
            return Response(
                {"error": "timer_seconds must be greater than 0"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            quiz = Quiz.objects.get(room_code=room_code)
        except Quiz.DoesNotExist:
            return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            rows = _fetch_opentdb_questions(
                amount=amount,
                category=category,
                difficulty=difficulty,
                question_type=question_type,
            )
        except URLError:
            return Response(
                {"error": "Unable to fetch questions from OpenTDB right now"},
                status=status.HTTP_502_BAD_GATEWAY,
            )
        except json.JSONDecodeError:
            return Response(
                {"error": "Invalid response from OpenTDB"},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        created_questions = 0
        created_options = 0

        with transaction.atomic():
            for row in rows:
                question = Question.objects.create(
                    quiz=quiz,
                    text=row["text"],
                    timer_seconds=timer_seconds,
                )
                created_questions += 1

                for option in row["options"]:
                    Option.objects.create(
                        question=question,
                        text=option["text"][:200],
                        is_correct=option["is_correct"],
                    )
                    created_options += 1

        return Response(
            {
                "room_code": quiz.room_code,
                "source": "OpenTDB",
                "requested_amount": amount,
                "created_questions": created_questions,
                "created_options": created_options,
                "total_questions_in_quiz": quiz.questions.count(),
            },
            status=status.HTTP_201_CREATED,
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
