# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime
# Create your views here.
def index(request):
    print strftime("%Y-%m-%d %H:%M %p", gmtime())
    print strftime("%Z %b %d, %Y at %H:%M %p",gmtime())
    context = {
        "time" : strftime("%z %b %d, %Y at %H:%M %p", localtime()),
    }
    return render(request, 'time_display_app/index.html', context)
