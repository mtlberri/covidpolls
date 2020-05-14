from django import forms
from .models import Parent1


# Form Class for the parent 1
class Parent1Form(forms.ModelForm):

    class Meta:
        model = Parent1
        fields = ['parent1_first_name', 'parent1_last_name', 'parent1_email_address',
                  'parent1_phone']
        labels = {
            'parent1_first_name': 'First name',
            'parent1_last_name': 'Last name',
            'parent1_email_address': 'E-mail',
            'parent1_phone': 'Phone number',
        }
        widgets = {
            'parent1_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent1_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent1_email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'parent1_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
