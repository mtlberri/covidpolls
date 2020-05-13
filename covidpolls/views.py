from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.urls import reverse

from .models import Child, Parent1
from .forms import Parent1Form


def get_parent_preferences(request):
    if request.method == 'POST':
        parent1_form = Parent1Form(request.POST)
        if parent1_form.is_valid():
            # Save in the DB
            new_parent1 = parent1_form.save()
            return HttpResponseRedirect(reverse('covidpolls:thanks'))
    # Else if method GET
    else:
        parent1_form = Parent1Form()
    context = {'form': parent1_form}
    return render(request, 'covidpolls/index.html', context)


def thanks(request):
    return render(request, 'covidpolls/thanks.html')

#
# def index(request):
#     return render(request, 'covidpolls/index.html')
#
#
# def save_form_in_db(request):
#     # Save the data in the DB
#     parent1 = Parent1(parent1_first_name=request.POST['parent1_first_name'],
#                       parent1_last_name=request.POST['parent1_last_name'],
#                       parent1_email_address=request.POST['parent1_email'],
#                       parent1_phone=request.POST['parent1_phone'])
#     parent1.save()
#
#     print('Date: ' + request.POST['date'])
#     if request.POST['date'] == '':
#         print('Date is empty, replace by standard date 2020-01-01')
#         date = '2020-01-01'
#     else:
#         print('Date is not empty and is:' + request.POST['date'])
#         date = request.POST['date']
#
#     parent1.child_set.create(
#         child_first_name=request.POST['child_first_name'],
#         child_last_name=request.POST['child_last_name'],
#         child_return_asap=request.POST['child_asap'] == 'Yes',
#         child_date_return=date,
#     )
#     child_name = request.POST['child_first_name']
#     return HttpResponseRedirect(reverse('covidpolls:confirmation', args=(child_name, )))
#
#
# def confirmation(request, child_name):
#     context = {'child_name': child_name}
#     return render(request, 'covidpolls/confirmation.html', context)
