# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
EMAIL_REGEX  = re.compile(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    confPassword = models.CharField(max_length = 255)
    authority = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return "id {}, fn {} ln {} em {} pass {}".format(self.id, self.first_name, self.last_name, self.email, self.password)
class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    writer = models.ForeignKey(User, related_name="messages")






class Validate(object):
    def go(request, postData):
        error = []
        try:
            a = User.objects.get(email = postData['em'])
            error.append("Email already in use")
            return error
        except:
            if not EMAIL_REGEX.match(postData['em']):
                error.append("Invalid Email Address")
            if len(postData['fn']) < 3:
                error.append("First name must be more than 3 characters")
            if len(postData['ln']) < 3:
                error.append("Last name must be more than 3 characters")
            if len(postData['pw']) < 5:
                error.append("Password must be more than 5 characters")
            if postData['pw'] != postData['cp']:
                error.append("Passwords must match")
            return error
    def login(request, postData):
        try:
            a = User.objects.get(email = postData['em'])
            if postData['pw'] == a.password:
                signIn = {
                    'first_name' : a.first_name,
                    'email' : a.email
                }
                return signIn
        except:
            return False
