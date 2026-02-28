from rest_framework import serializers
from .models import Question,Quiz,Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id' , 'text']
  
  
  
        
class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    
    class Meta:
        models = Question
        fields = ['id' , 'text' , 'timer_seconds' , 'options']
     
     
     
        
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'room_code', 'questions']