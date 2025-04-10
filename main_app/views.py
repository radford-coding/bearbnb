from ast import Del
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cave, Hibernation
from .forms import HibernationForm

# Create your views here.


class Home(LoginView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class CaveIndex(LoginRequiredMixin, ListView):
    model = Cave


class CaveDetail(LoginRequiredMixin, DetailView):
    model = Cave

    def get_queryset(self):
        return Cave.objects.all()  # maybe get just one?

    def get_context_data(self, **kwargs):
        form = HibernationForm()
        context = super().get_context_data(**kwargs)
        if not kwargs.get('form'):
            context['form'] = form
        return context

    def post(self, request, pk):
        form = HibernationForm(request.POST)
        form.instance.bear = request.user
        form.instance.cave = Cave.objects.get(id=pk)
        if form.is_valid():
            form.save()
            return redirect('cave-detail', pk=pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class CaveCreate(LoginRequiredMixin, CreateView):
    model = Cave
    fields = ['name', 'rate', 'sleeps', 'address',
              'city', 'state', 'zipcode', 'description', 'image']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CaveUpdate(LoginRequiredMixin, UpdateView):
    model = Cave
    fields = ['name', 'rate', 'sleeps', 'description']


class CaveDelete(LoginRequiredMixin, DeleteView):
    model = Cave
    success_url = '/caves/'


def signup(request):
    error_msg = ''
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cave-index')
        else:
            # needs more descriptive feedback. also doesn't work...
            error_msg = 'Invalid sign-up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'signup.html', context)


# class HibernationCreateView(LoginRequiredMixin, CreateView):
#     model = Hibernation
#     fields = ['start_date', 'nights']

# class HibernationUpdateView(LoginRequiredMixin, UpdateView):
#     model = Hibernation
#     fields = ['start_date', 'nights']

# class HibernationDeleteView(LoginRequiredMixin, DeleteView):
#     model = Hibernation
#     success_url = '/caves/'
