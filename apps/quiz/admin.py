from django.contrib import admin

from quiz.models import Question, Result, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    fk_name = 'question'
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['title', 'quiz']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Result)
