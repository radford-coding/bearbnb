from django import forms
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