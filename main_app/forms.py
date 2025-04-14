from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from localflavor.us.forms import USStateSelect
from .models import Cave, Hibernation


class HibernationForm(forms.ModelForm):
    class Meta:
        model = Hibernation
        fields = ['start_date', 'nights']
        widgets = {
            'start_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Pick a date',
                    'type': 'date',
                }
            )
        }
