# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User, Book, Review
# Create your views here.
def index(request):
    if 'logged' in request.session:
        return redirect('/book')
    else:
        return render(request, 'belt_app/login.html')
def show(request):
        content = {
        'books' : Book.objects.all(),
        'reviews' : Review.objects.all()
        }
        return render(request, 'belt_app/index.html', content)
def create(request):
    # ----------------------------User creation
    if 'em' in request.POST:
        user = User.objects.create(first_name = request.POST['fn'], last_name = request.POST['ln'], email =request.POST['em'], password = request.POST['pw'])
        print user
        logged = {
            "first" : user.first_name,
            "id" : user.id
        }
        request.session['logged'] = logged
        return redirect('/')
    # ------------------------------------
    else:
        currentid = request.session['logged']['id']
        user = User.objects.get(id = currentid)
        book = Book.objects.create(title = request.POST['ti'], author = request.POST['au'])
        rev = Review.objects.create(book = book, user = user, stars = request.POST['stars'], content = request.POST['de'] )
        # rev.book.add(book)
        # rev.user.add(user)
        return redirect('/')



def clear(request):
    request.session.clear()
    a = User.objects.all()
    b = Review.objects.all()
    c = Book.objects.all()
    a.delete()
    b.delete()
    c.delete()
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
def showbook(request, number):
    rev = Review.objects.get(id = number)
    content = {
        'book' : rev
    }
    return render(request, 'belt_app/books.html',content)
