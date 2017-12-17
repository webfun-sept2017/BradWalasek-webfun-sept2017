# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "id number {}, {}, book about {}".format(self.id, self.name, self.desc)
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    books = models.ManyToManyField(Book, related_name = "authors")
    notes = models.TextField()
    notes = "none"
    def __str__(self):
        # return "{} {} wrote {}".format(self.first_name, self.last_name, self.books)
        return "id = {}, {} {}".format(self.id, self.first_name, self.last_name)
