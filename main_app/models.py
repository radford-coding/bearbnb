from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField

# Create your models here.

class Cave(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField()
    sleeps = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=45)
    state = USStateField()
    zipcode = USZipCodeField()
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)