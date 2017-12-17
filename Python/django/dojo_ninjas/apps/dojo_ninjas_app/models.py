# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    desc = "empty"
    def __str__(self):
        return "Dojo id {}, named {} at {}, {}".format(self.id, self.name, self.city, self.state)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id =models.ForeignKey(Dojo, related_name="ninjas")
    def __str__(self):
        return "id: {}, {} {} at {}".format(self.id, self.first_name, self.last_name, self.dojo_id.name)
