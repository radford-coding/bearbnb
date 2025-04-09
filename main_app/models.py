from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField
from django.core.validators import MaxValueValidator

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

