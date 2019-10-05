from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class userprofile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE),
    phone = models.CharField(max_length=15)
    gender = models.BooleanField(default=False)
    address = models.CharField(max_length=150)

# model for extending and storing user data
class profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)


