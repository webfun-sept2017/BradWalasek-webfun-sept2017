# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
def test(request):
    response = "This is the test method"
    return HttpResponse(response)
def show(response,number):
    print number
    return HttpResponse("Show method " + number)
def show_word(response, word):
    return HttpResponse("Show_word method " + word)
def year_archive(response,year):
    return HttpResponse("Year_archive method " + year)
def month_archive(response, year, month):
    return HttpResponse("month_archive method " + year + " " + month)
