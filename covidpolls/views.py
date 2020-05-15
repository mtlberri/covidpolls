from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.urls import reverse

from .models import ParentChildPreference
from .forms import ParentChildPreferenceForm


def get_parent_preferences(request):
    if request.method == 'POST':
        form = ParentChildPreferenceForm(request.POST)
        if form.is_valid():
            # Save in the DB
            new_preference_form = form.save()
            return HttpResponseRedirect(reverse('covidpolls:thanks'))
    # Else if method GET
    else:
        form = ParentChildPreferenceForm()
    context = {'form': form}
    return render(request, 'covidpolls/index.html', context)


def thanks(request):
    return render(request, 'covidpolls/thanks.html')

