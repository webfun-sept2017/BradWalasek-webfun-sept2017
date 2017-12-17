# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
        'num' : get_random_string(length=14)
    }
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1
    return render(request, "number_generator/index.html",context)
def reset(request):
    request.session['attempt'] = 0
    return redirect('/random_word')
