from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.urls import reverse

from .models import ParentChildPreference
from .forms import ParentChildPreferenceForm


def get_parent_preferences(request):
    if request.method == 'POST':
        form = ParentChildPreferenceForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            print(f'Date field value is :{form.cleaned_data["child_date_return"]}')
            # Save in the DB
            new_preference_form = form.save()
            return HttpResponseRedirect(reverse('covidpolls:thanks'))
        else:
            print(f'Form is not valid, errors:{form.errors}')
    # Else if method GET
    else:
        form = ParentChildPreferenceForm()
    context = {'form': form}
    return render(request, 'covidpolls/index.html', context)


def thanks(request):
    return render(request, 'covidpolls/thanks.html')

