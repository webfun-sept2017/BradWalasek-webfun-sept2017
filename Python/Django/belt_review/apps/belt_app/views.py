# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User, Review
# Create your views here.
def index(request):
    if 'logged' in request.session:

        return redirect('/book')
    else:
        content = {
        'users' : User.objects.all()
        }
        print content
    return render(request, 'belt_app/login.html', content)
def show(request):
        content = {
        'reviews' : Review.objects.all()
        }
        return render(request, 'belt_app/index.html', content)
def create(request):
    if 'em' in request.POST:
        user = User.objects.create(first_name = request.POST['fn'], last_name = request.POST['ln'], email =request.POST['em'], password = request.POST['pw'])
        print user
        logged = {
            "first" : user.first_name,
            "last"  : user.last_name,
            "id" : user.id,
            'email' : user.email
        }
        request.session['logged'] = logged
        return redirect('/')
    else:
        # user = User.objects.get(id = request.session['logged']['id'])
        review = Review.objects.create(book = request.POST['ti'], desc = request.POST['de'], stars = request.POST['stars'])
        a = User.objects.get(id = request.session['logged']['id'])
        print a

        review.user.add(a)
        return redirect('/book')
def clear(request):
    request.session.clear()
    a = User.objects.all()
    b = Review.objects.all()
    a.delete()
    b.delete()
    return redirect ('/')
def login(request):
    try:
        ver = User.objects.get(email = request.POST['em'])
        if ver.password == request.POST['pw']:
            print "correct password"
            logged = {
                "first" : ver.first_name,
                "last"  : ver.last_name,
                "id" : ver.id,
                'email' : ver.email
            }
            request.session['logged'] = logged

    except:
        print 'invalid email address'
    return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')
def add(request):
    return render(request, 'belt_app/add.html')
def showbook(request, string):
    rev = Review.objects.get(book = string)
    print 'here'
    print rev.book
    content = {
        'book' : rev
    }
    return render(request, 'belt_app/books.html',content)
