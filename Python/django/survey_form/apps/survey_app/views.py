# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'survey_app/index.html')
def process(request):

    request.session['name'] = request.POST['name']
    request.session['loc'] = request.POST['loc']
    request.session['lang'] = request.POST['lang']
    request.session['com'] = request.POST['com']



    return redirect('/result')

def result(request):
    print "*"*80
    print request.session['name']
    print request.session['loc']
    print request.session['lang']
    print request.session['com']
    if 'submit' in request.session:
        request.session['submit'] += 1
    else:
        request.session['submit'] = 0
    return render(request, 'survey_app/result.html')
