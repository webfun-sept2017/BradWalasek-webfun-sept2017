# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Review(models.Model):
    book = models.CharField(max_length=255)
    desc = models.CharField(max_length = 255)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ManyToManyField(User, related_name="reviews")
