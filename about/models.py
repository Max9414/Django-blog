from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField
    created_on = models.DateTimeField(auto_now=True)
