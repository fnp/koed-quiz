from django.shortcuts import render
#from django.contrib.sites import Site

from django.conf import settings
from quiz.models import Quiz


def home(request):
    quiz = Quiz.current()
    return render(request, "home.html", locals())
