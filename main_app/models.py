from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cave(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField()
    sleeps = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    zipcode = models.IntegerField()
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)