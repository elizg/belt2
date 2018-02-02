from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name=models.CharField(max_length=64)
    user_name=models.CharField(max_length=64)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=64)
    hired=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
