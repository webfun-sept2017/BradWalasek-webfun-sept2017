# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User, Val
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


# Create your views here.
def index(request):
    info = {
        'users' : User.objects.all(),
    }
    return render(request, 'Semi_Restful_Users_app/index.html',info)
def show(request, number):
    info = {
        'user' : User.objects.get(id  = number),
    }
    return render(request, "Semi_Restful_Users_app/user_info.html",info)
def edit(request, number):
    info = {
        'user' : User.objects.get(id = number),
    }
    return render(request, 'Semi_Restful_Users_app/edit.html', info)

def destroy(request, number):
    a = User.objects.get(id = number)
    a.delete()
    a.save
    return redirect('/users')
def new(request):
    return render(request, 'Semi_Restful_Users_app/new.html')
def create(request):
    newVal = Val()
    error = newVal.go(request.POST)
    print "$"*50
    print error
    if len(error) > 0:
        for key, val in error.items():
            print val
            print "*"*50
            messages.add_message(request, messages.INFO, val)
            return redirect('/new')
    else:
        User.objects.create(name = request.POST['name'], email = request.POST['email'])
        a = User.objects.last().id
        return redirect('/users/'+ str(a))
def update(request, number):
    a = User.objects.get(id = number)
    a.name = request.POST['name']
    a.email = request.POST['email']
    a.save()
    return redirect ('/users/' + str(a.id))
