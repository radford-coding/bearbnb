from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
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


class SearchForm(forms.ModelForm):
    class Meta:
        model = Cave
        fields = ['city']
