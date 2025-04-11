from urllib import request
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
import os


# Create your models here.


class Cave(models.Model):
    name = models.CharField(max_length=100)
    rate = models.PositiveIntegerField(validators=[MaxValueValidator(1000)])
    sleeps = models.PositiveIntegerField(validators=[MaxValueValidator(50)])
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=45)
    state = USStateField()
    zipcode = USZipCodeField()
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse("cave-detail", kwargs={"pk": self.id})

# user profile
# class Bear(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.TextField()
    cave = models.ForeignKey(Cave, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for cave_id: {self.cave_id} @{self.url}'

class Hibernation(models.Model):
    start_date = models.DateField('First night')
    nights = models.PositiveIntegerField(validators=[MaxValueValidator(90), MinValueValidator(1)])
    cave = models.ForeignKey(Cave, on_delete=models.CASCADE)
    bear = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nights} {'nights' if self.nights > 1 else 'night'} in: {self.cave.name} ({self.id})'
    
    # def get_absolute_url(self):
    #     return reverse("hibernation-detail", kwargs={"pk": self.id})
    
