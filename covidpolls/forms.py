from django import forms
from .models import ParentChildPreference


# Form Class for the parent 1
class ParentChildPreferenceForm(forms.ModelForm):

    class Meta:
        model = ParentChildPreference
        fields = ['parent_first_name', 'parent_last_name', 'parent_email_address',
                  'parent_phone', 'child_first_name', 'child_last_name',
                  'child_return_asap', 'child_date_return']
        labels = {
            'parent_first_name': 'Parent First name',
            'parent_last_name': 'Parent Last name',
            'parent_email_address': 'E-mail',
            'parent_phone': 'Phone number',
            'child_first_name': 'Child First name',
            'child_last_name': 'Child Last name',
            'child_return_asap': 'Do you wish you child to come back as soon as possible?',
            'child_date_return': 'If no, required date of return',
        }
        widgets = {
            'parent_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'parent_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'child_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'child_last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
