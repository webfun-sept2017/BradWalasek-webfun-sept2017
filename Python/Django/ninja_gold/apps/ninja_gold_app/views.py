# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

import time
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'ninja_gold_app/index.html')
def process(request):

    if 'log' not in request.session:
        request.session['log'] = []
        request.session['gold'] = 0
    money = determine(request.POST['action_id'])
    request.session['gold'] += money[0]
    print money[0]
    print request.session['gold'], "Gold"
    print "*"*100
    if money[0]<0:
        # print 'Lost ' + str(abs(money[0])) + ' from the ' + money[1] + "... Ouch." + money[2]
        listitem = 'Lost ' + str(abs(money[0])) + ' from the ' + money[1] + "... Ouch." + money[2]
    else:
        # print 'Earned ' + str(money[0]) + ' from the ' + money[1] + "!" + money[2]
        listitem = 'Earned ' + str(money[0]) + ' from the ' + money[1] + "!" + money[2]
    # print "The action id is ", request.POST['action_id']
    # print "PT Process"
    # print money
    print "*"*100
    request.session['log'].insert(0,listitem)
    request.session.modified = True
    print request.session['log']
    if len(request.session['log']) >8:
        request.session['log'].pop(8)

    return redirect('/ninja_gold')

def refresh(request):
    request.session.clear()
    return redirect('/ninja_gold')

def determine(val):
    earned = 0
    if val == '1':
        earned = farm()
    if val == '2':
        earned = cave()
    if val == '3':
        earned = house()
    if val == '4':
        earned = casino()
    earned.append(time.strftime("(%Y/%m/%d %H:%M %p)",time.localtime()))
    return earned;

def farm():
    x = [random.randint(10, 20), 'farm']
    return x

def cave():
    x = [random.randint(5, 10), 'cave']
    return x

def house():
    x = [random.randint(2, 5), 'house']
    return x

def casino():
    x = [random.randint(-50, 50), 'casino']
    return x
