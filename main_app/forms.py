from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from localflavor.us.forms import USStateSelect
from .models import Cave, Hibernation

class CaveForm(forms.ModelForm):
    class Meta:
        model = Cave
        fields = ['name', 'rate', 'sleeps', 'address', 'city', 'state', 'zipcode', 'description']
        widgets = {
            'state': USStateSelect(
                attrs={
                    'placeholder': 'Choose a state'
                }
            )
        }

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

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=200)

#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2']