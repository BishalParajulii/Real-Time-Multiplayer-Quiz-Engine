from rest_framework import serializers

from .models import Option, Question, Quiz


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "text"]


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "text", "timer_seconds", "options"]


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    host_id = serializers.IntegerField(source="host.id", read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "room_code", "host_id", "questions"]
