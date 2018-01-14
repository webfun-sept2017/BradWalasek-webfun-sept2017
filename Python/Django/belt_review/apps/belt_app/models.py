# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length = 255)

class Review(models.Model):
    book = models.ForeignKey(Book, related_name = "reviews")
    user = models.ForeignKey(User, related_name = "reviews")
    content = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
