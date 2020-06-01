from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Choice, User
from django.http import JsonResponse
import json


def compoll_question(request):
    """View displaying a Question and associated Choices, and managing the Vote"""
    if request.method == 'POST':
        pass
    # Else if method GET
    else:
        question = Question.objects.all().first()
        choice_a = question.choice_set.filter(choice='A').get()
        # print(f'Choice A: {choice_a}')
        # print(f'Choice A voters: {choice_a.voters.all()}')
        choice_b = question.choice_set.filter(choice='B').get()
        # print(f'Choice B: {choice_b}')
        # print(f'Choice B voters: {choice_b.voters.all()}')
        context = {'question': question, 'choice_a': choice_a, 'choice_b': choice_b}
    return render(request, 'compolls/question.html', context)


def manage_vote(request):
    """View managing the vote actions via AJAX"""
    body = json.loads(request.body)
    print('user :' + body['user'])
    print('choice_id: ' + body['choice_id'])
    user_name = body['user']
    try:
        choice_id = int(body['choice_id'])
    except:
        print('Could not cast the choice_id into integer type')
    # Save the user vote for that choice in the DB
    user, _ = User.objects.get_or_create(name=user_name)
    choice = Choice.objects.get(pk=choice_id)
    choice.voters.add(user)
    returned_data = {
        'user': str(user),
        'choice_id': choice.id,
    }
    return JsonResponse(returned_data)

