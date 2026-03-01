from django.urls import path

from .views import (
    BulkQuestionCreateView,
    CategoryListView,
    JoinQuizView,
    OpenTDBImportView,
    QuizCreateView,
    create_room,
    index,
    room,
)

app_name = "quiz"

urlpatterns = [
    # Frontend pages
    path("", index, name="index"),
    path("create-room/", create_room, name="create-room"),
    path("room/<str:room_code>/", room, name="room"),
    # API endpoints
    path("api/quiz/categories/", CategoryListView.as_view(), name="quiz-categories"),
    path("api/quiz/create/", QuizCreateView.as_view(), name="quiz-create"),
    path("api/quiz/join/", JoinQuizView.as_view(), name="quiz-join"),
    path("api/quiz/questions/bulk/", BulkQuestionCreateView.as_view(), name="quiz-questions-bulk"),
    path("api/quiz/questions/import-opentdb/", OpenTDBImportView.as_view(), name="quiz-questions-import-opentdb"),
]
