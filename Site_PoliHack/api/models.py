from django.db import models
import string
import random
# Create your models here.

class Clasa(models.Model):
    cod = models.CharField(max_length=8, default='', unique=True)
    profesor = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
