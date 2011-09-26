from django.contrib import admin

from quiz.models import Quiz, Question, Result, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = 'question'
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['title', 'quiz']


class ResultAdmin(admin.ModelAdmin):
    list_display = ['title', 'quiz']


class QuizAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Quiz, QuizAdmin)
