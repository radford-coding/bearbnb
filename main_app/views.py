from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.

class Home(LoginView):
    template_name = 'home.html'