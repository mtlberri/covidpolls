from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Choice, User
from django.http import JsonResponse
import json
from django.core import serializers


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
    print('user received:' + body['user'])
    print('choice_id received: ' + body['choice_id'])
    user_name = body['user']
    try:
        choice_id = int(body['choice_id'])
    except:
        print('Could not cast the choice_id into integer type')
    # Save the user vote for that choice in the DB
    user, _ = User.objects.get_or_create(name=user_name)
    choice = Choice.objects.get(pk=choice_id)
    choice.voters.add(user)

    # Get list of voters for A and B
    question = choice.question
    choice_a = question.choice_set.filter(choice='A').get()
    choice_b = question.choice_set.filter(choice='B').get()

    lst_voters_users_a = list(choice_a.voters.all())
    lst_voters_users_b = list(choice_b.voters.all())

    dict_voters_names = {
        'voters_for_a': [x.__str__() for x in lst_voters_users_a],
        'voters_for_b': [x.__str__() for x in lst_voters_users_b],
    }
    print('Voters to be returned to client')
    print(dict_voters_names)
    # Get list of voters for B
    voters_for_b = []
    returned_data = {
        'user': str(user),
        'choice_id': choice.id,
        'voters': dict_voters_names,
    }
    return JsonResponse(returned_data)

