from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cave

# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class CaveIndex(ListView):
    model = Cave