from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm
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

class CaveDetail(DetailView):
    model = Cave

class CaveCreate(CreateView):
    model = Cave
    fields = ['name', 'rate', 'sleeps', 'address', 'city', 'state', 'zipcode', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def signup(request):
    error_msg = ''
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cave-index')
        else:
            print(form)
            error_msg = 'Invalid sign-up try again'

    form = UserCreationForm()
    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'signup.html', context)