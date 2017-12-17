# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Course
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, "courses_app/index.html", context)
def create(request):
    # print request.POST['name']
    # print request.POST['desc']
    Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    # print '*'*50
    # print Course.objects.all()
    return redirect('/')
def remove(request, var):
    context = {
        'rem' : Course.objects.get(id = var)
    }
    return render(request, 'courses_app/destroy.html', context)

def destroy(request, var):
    a = Course.objects.get(id = var)
    a.delete()
    return redirect('/')
