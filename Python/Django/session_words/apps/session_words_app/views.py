# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "session_words_app/index.html")
def process(request):
    tuple1 = (request.POST['color'],request.POST['check'], request.POST['word'])
    print "*" * 100
    if 'count' in request.session:

        print "count exists"
        request.session['count'] += 1
        request.session[request.session['count']] = tuple1


    else:

        print "Creating new request.session['test']"
        request.session['count'] = 0
        request.session[request.session['count']] = tuple1

    print request.session['count']
    print request.session[request.session['count']]

    print "*" * 100
    return redirect('/')
def clear(request):
    a = request.session['count']
    for x in range(0,a):
        print "counting " + str(x) + " out of " + str(a)

        if x in request.session:
            print "clearing " + str(x)
            request.session.pop(x)

    request.session.pop('count')
    print "clearing ['count']"
    return redirect('/')
