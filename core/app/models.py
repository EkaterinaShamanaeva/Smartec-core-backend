# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.TextField()
    password = models.TextField()
