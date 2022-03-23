from email.policy import default
from django.db import models

# Create your models here.


class items(models.Model):
    modelname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    gib = models.FileField(upload_to="images")
    price = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    modeltype = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    fbx = models.FileField(upload_to="images")
