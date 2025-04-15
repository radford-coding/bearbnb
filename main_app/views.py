from ast import Del
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Cave, Hibernation, Photo
from .forms import HibernationForm, ProfileForm
import uuid
import boto3
from dotenv import load_dotenv
import os
load_dotenv()


# Create your views here.


class Home(LoginView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class CaveIndex(LoginRequiredMixin, ListView):
    model = Cave


class CaveDetail(LoginRequiredMixin, DetailView):
    model = Cave

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
              'city', 'state', 'zipcode', 'description']

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cave-index')
        else:
            error_msg = 'Invalid sign-up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_msg': error_msg}
    return render(request, 'signup.html', context)


def add_photo(request, cave_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.getenv('S3_BUCKET')
            s3.upload_fileobj(photo_file, bucket, key)
            url = f'{os.getenv('S3_BASE_URL')}{bucket}/{key}'
            Photo.objects.create(url=url, cave_id=cave_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('cave-detail', pk=cave_id)


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
