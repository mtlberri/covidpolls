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
            'child_first_name': 'First name',
            'child_last_name': 'Last name',
            'parent_first_name': 'First name',
            'parent_last_name': 'Last name',
            'parent_email_address': 'E-mail',
            'parent_phone': 'Phone number',
        }
        widgets = {
            'parent_first_name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'First name'}),
            'parent_last_name': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Last name'}),
            'parent_email_address': forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'name@example.com'}),
            'parent_phone': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': '(514)-555-5555'}),
            'child_first_name': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'First Name'}),
            'child_last_name': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Last Name'}),
            'child_return_asap': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')], attrs={'class': 'form-check-input'}),
            'child_date_return': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
