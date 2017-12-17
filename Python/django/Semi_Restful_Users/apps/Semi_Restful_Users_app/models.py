# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
from django.contrib import messages
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return "id: {}, name: {}, email {}".format(self.id, self.name, self.email)
class Val(models.Model):
    def go(self, postData):
        print postData
        error = {}
        if len(postData['name']) < 3:
            error['name']='Name must be more than 3 characters'
        if len(postData['email']) <5:
            error['email']="Email must be more than 5 characters"
            print error
        return error
