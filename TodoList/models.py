from os import name
from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=150)
    priority = models.IntegerField()
    completed = models.BooleanField(default=0)
