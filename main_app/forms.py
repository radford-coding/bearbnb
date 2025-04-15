from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Hibernation


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

class ProfileForm(ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email']
