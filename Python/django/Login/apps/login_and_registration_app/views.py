# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User, Validation
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
# Create your views here.
def index(request):
    if 'logged' in request.session:
        request.session['status'] = "Successfully logged in!"
        return redirect('/success')
    content = {
        "all" : User.objects.all(),
    }
    return render(request, 'login_and_registration_app/index.html', content)
def success(request):
    return render(request, 'login_and_registration_app/success.html')
def create(request):
    Val = Validation()
    ver = Val.act(request.POST)
    print "***"
    print ver
    if len(ver) > 0:
        for item in ver:
            messages.add_message(request, messages.INFO, item)
        return redirect('/')
    else:
        user = User.objects.create(first_name = request.POST['fn'], last_name = request.POST['ln'], email = request.POST['em'], password = request.POST['pw'])
        signIn = {
            'first_name' : user.first_name,
            'email' : user.email
        }
        request.session['logged'] = signIn
        request.session['status'] = "Successfully registered!"
        return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')
def clear(request):
    a = User.objects.all()
    a.delete()
    request.session.clear()
    return redirect('/')
def login(request):
    Val = Validation()
    user = Val.login(request.POST)
    print "***"
    print user
    if user == False:
        messages.add_message(request, messages.INFO, "Invalid Email/Password")
    else:
        request.session['logged'] = user
    return redirect('/')
