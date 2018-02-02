from __future__ import unicode_literals
from django.db import models
from ..main.models import User

class Item(models.Model):
    title=models.CharField(max_length=64)
    user=models.ForeignKey(User, related_name='items')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Wish(models.Model):
    wish=models.ForeignKey(Item, related_name='wishers')
    wisher=models.ForeignKey(User, related_name='wishes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

