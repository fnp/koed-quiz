from .models import Quiz

class CurrentQuizMiddleware(object):
    def process_request(self, request):
        request.current_quiz = Quiz.current(request)
