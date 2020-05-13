from django.forms import ModelForm
from .models import Parent1


# Form Class for the parent 1
class Parent1Form(ModelForm):
    class Meta:
        model = Parent1
        fields = ['parent1_first_name', 'parent1_last_name', 'parent1_email_address',
                  'parent1_phone']
