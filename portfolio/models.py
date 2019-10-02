from django.db import models


# Create your models here.

class Portfolio(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=30)
    summery = models.CharField(max_length=200)
