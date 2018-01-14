# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "session_words_app/index.html")
def process(request):
    if not 'color' in request.POST:
        return redirect('/')
    mydict = {
        "color" : request.POST['color'],
        "word" : request.POST['word'],
    }
    if not 'size' in request.POST:
        mydict['size'] = "small"
    else:
        mydict['size'] = 'large'

    print mydict
    if 'list' in request.session:
        request.session['list'].append(mydict)
    else:
        request.session['list'] = []

        request.session['list'].append(mydict)
    print request.session['list']
    request.session['count'] = len(request.session['list'])
    request.session.modified = True
    # tuple1 = (request.POST['color'],request.POST['check'], request.POST['word'])
    # print "*" * 100
    # if 'count' in request.session:
    #
    #     print "count exists"
    #     request.session['count'] += 1
    #     request.session[request.session['count']] = tuple1
    #
    #
    # else:
    #
    #     print "Creating new request.session['test']"
    #     request.session['count'] = 0
    #     request.session[request.session['count']] = tuple1
    #
    # print request.session['count']
    # print request.session[request.session['count']]
    #
    # print "*" * 100

    return redirect('/')
def clear(request):
    print 'this works'
    request.session.clear()
    return redirect('/')
