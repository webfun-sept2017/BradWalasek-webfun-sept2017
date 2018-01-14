# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import Validate, User
from django.contrib import messages

# Create your views here.
def index(request):
    content = {
        'users' : User.objects.all()
    }

    if 'logged' in request.session:
        print request.session['logged']
        return render(request, "User_Dashboard_app/dashboard.html", content)
    else:
        return redirect('/login')
# def login(request):
#     return render(request, 'User_Dashboard_app/login.html')
def show(request, number):
    print number
    try:
        content = {
            'user' : User.objects.get(id = number)
        }
        return render(request, "User_Dashboard_app/show.html", content)
    except:
        return redirect('dashboard')
def new(request):
    # render register page
    return render(request, 'User_Dashboard_app/register.html')
def create(request):
    val = Validate()
    error = val.go(request.POST)
    print error
    if len(error)>0:
        for issue in error:
            messages.add_message(request, messages.INFO, issue)
        return redirect ('/new')
    else:
        User.objects.create(first_name = request.POST['fn'], last_name = request.POST['ln'], email = request.POST['em'], password = request.POST['pw'])

        user = User.objects.get(email = request.POST['em'])
        if user == User.objects.first():
            user.authority = "admin"
            user.save()
        else:
            user.authority = "normal"
            user.save()

        currentUser = {
            'name' : user.first_name,
            'id' : user.id,
        }
        request.session['logged'] = currentUser
        return redirect('/')
def clear(request):
    a = User.objects.all()
    a.delete()
    request.session.clear()
    return redirect('/login')
def logout(request):
    request.session.clear()
    return redirect('/login')
def login(request):

    content = {
        'users' : User.objects.all()
    }

    if request.method == "GET":
        return render(request, 'User_Dashboard_app/login.html', content)
    else:
        Val = Validate()
        user = Val.login(request.POST)
        print "***"
        print user
        if user == False:
            messages.add_message(request, messages.INFO, "Invalid Email/Password")
            return redirect('/login')
        else:
            request.session['logged'] = user
        return redirect('/')
