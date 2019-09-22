from django.utils.deprecation import MiddlewareMixin
from .models import Quiz

class CurrentQuizMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.current_quiz = Quiz.current(request)
