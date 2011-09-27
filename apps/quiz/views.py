from django.shortcuts import get_object_or_404, render, redirect

from quiz.forms import QuestionForm
from quiz.models import Quiz


def question(request, slug=None):
    if slug is None:
        question = Quiz.current().start()
        request.session['ticket'] = [request.path]
    else:
        question = get_object_or_404(Quiz.current().question_set, slug=slug)

    ticket = request.session.get('ticket', [])
    valid = request.path in ticket

    if valid:
        cur_index = ticket.index(request.path)
        if cur_index:
            previous_url = ticket[cur_index - 1]
    elif ticket:
        valid_url = ticket[-1]

    if request.method == 'POST' and valid:
        form = QuestionForm(question, request.POST)
        if form.is_valid():

            answer = form.cleaned_data['answer']
            where_to = answer.where_to()

            del ticket[cur_index + 1:]
            try:
                del ticket[ticket.index(where_to) + 1:]
            except ValueError:
                ticket.append(where_to)

            request.session['ticket'] = ticket

            return redirect(where_to)
    else:
        form = QuestionForm(question)

    return render(request, "quiz/question_detail.html", locals())


def result(request, slug=None):
    ticket = request.session.get('ticket', [])
    valid = request.path in ticket

    if valid:
        cur_index = ticket.index(request.path)
        if cur_index:
            previous_url = ticket[cur_index - 1]
    elif ticket:
        valid_url = ticket[-1]

    result = get_object_or_404(Quiz.current().result_set, slug=slug)
    return render(request, "quiz/result_detail.html", locals())

