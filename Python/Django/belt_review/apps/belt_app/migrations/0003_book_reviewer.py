# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reviewer',
            field=models.ManyToManyField(related_name='books', to='belt_app.User'),
        ),
    ]
