from django.db import models
from django.contrib.auth.models import User
import string, random


def generate_random_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    host = models.ForeignKey(User, on_delete=models.CASCADE , related_name='hosted_quizzes')
    room_code = models.CharField(max_length=6, unique=True, default=generate_random_code)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.room_code})"
    
    
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='question' , on_delete=models.CASCADE)
    text = models.TextField()
    timer_seconds = models.IntegerField(default=15)
    
    def __str__(self):
        return self.text
    
class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()
    
    def __str__(self):
        return self.text
    
class PlayerAnswer(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)  # calculated later

    def __str__(self):
        return f"{self.player.username} - {self.question.text[:20]}"