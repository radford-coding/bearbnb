from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from localflavor.us.forms import USStateSelect
from .models import Cave

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

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']