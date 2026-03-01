from django.contrib import admin

from .models import Option, PlayerAnswer, Question, Quiz


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "room_code", "host", "created_at")
    search_fields = ("title", "room_code", "host__username")
    inlines = [QuestionInline]


class OptionInline(admin.TabularInline):
    model = Option
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "quiz", "text", "timer_seconds")
    search_fields = ("text", "quiz__title", "quiz__room_code")
    inlines = [OptionInline]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "text", "is_correct")
    list_filter = ("is_correct",)
    search_fields = ("text", "question__text", "question__quiz__title")


@admin.register(PlayerAnswer)
class PlayerAnswerAdmin(admin.ModelAdmin):
    list_display = ("player", "question", "selected_option", "score")
    search_fields = ("player__username", "question__text")
