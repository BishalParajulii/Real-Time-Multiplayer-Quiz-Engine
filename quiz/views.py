from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth .models import User
from .models import Quiz
from .serializers import QuizSerializer , OptionSerializer


class QuizCreateView(APIView):
    def post(sqlf, request):
        host_id = request.data.get('host_id')
        title = request.data.get('title')
        
        if not host_id or not title:
            return Response({"error" : "host_id and title are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        host = User.objects.get(id=host_id)
        quiz = Quiz.objects.create(title=title, host = host)
        
        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class JoinQuizView(APIView):
    def post(self, request):
        room_code = request.data.get('room_code')
        player_id = request.data.get('player_id')

        if not room_code or not player_id:
            return Response({"error": "room_code and player_id are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            quiz = Quiz.objects.get(room_code=room_code)
        except Quiz.DoesNotExist:
            return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)

        player = User.objects.get(id=player_id)
        

        serializer = QuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)
        