from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Choice


def compoll_question(request):
    """View displaying a Question and associated Choices, and managing the Vote"""
    if request.method == 'POST':
        pass
    # Else if method GET
    else:
        user = 'Joffrey'
        question = Question.objects.get(pk=2)
        choice_a = question.choice_set.filter(choice='A').get()
        choice_b = question.choice_set.filter(choice='B').get()
        context = {'question': question, 'choice_a': choice_a, 'choice_b': choice_b}
    return render(request, 'compolls/question.html', context)


