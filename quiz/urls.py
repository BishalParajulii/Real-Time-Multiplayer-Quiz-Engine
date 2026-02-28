from django.urls import path
from .views import QuizCreateView, JoinQuizView

urlpatterns = [
    path('create/', QuizCreateView.as_view(), name='quiz-create'),
    path('join/', JoinQuizView.as_view(), name='quiz-join'),
]