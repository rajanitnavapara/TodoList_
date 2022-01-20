from os import name
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=150)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    user = models.CharField(max_length=32,default="None")
    # userd = models