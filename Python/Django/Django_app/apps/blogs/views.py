# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    context={
        "blogs" : Blog.objects.all(),
        "first_blog": Blog.objects.first(),
        'leng' : Blog.objects.count()
    }
    print context['leng']
    return render(request, 'blogs/index.html', context)
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def show(request, number):
    response = "placeholder to display blog " + number
    return HttpResponse(response)
def update(request,number):
    print number
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print tag, error
        return redirect('/')
    else:
        blog = Blog.objects.get(id = number)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        return redirect('/')
def destroy(request, number):
    a = Blog.objects.get(id = number)
    a.delete()
    return redirect('/')
def create(request):
    print ('Create')
    print request.POST['name']
    print request.POST['desc']
    Blog.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    return redirect('/')
