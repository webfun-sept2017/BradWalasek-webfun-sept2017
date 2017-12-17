# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    # print request.session
    return render(request, 'amadon_app/index.html')
def checkout(request):
    # print request.session['total']
    if 'total' not in request.session or request.session['total'] == 0:
        return redirect('/amadon')
    return render(request, 'amadon_app/checkout.html')
def basket(request):

    if 'list' not in request.session:
        request.session['list'] = []

    if 'overall' not in request.session:
        request.session['overall'] = 0
        request.session['quan'] = 0

    if 'item_id' in request.POST:
        print request.POST['item_id'], request.POST['quantity']
        item = handleitems(request.POST['item_id'], request.POST['quantity'])
        print item
        request.session['list'].append(item)
        request.session['quan'] += int(item[2])
        request.session['overall'] += float(item[3])

    request.session.modified = True




    print request.session['list']

    return render(request, 'amadon_app/basket.html')
def purchase(request):
    request.session['total'] = 0
    for item in request.session['list']:
        request.session['total'] += item[3]
    return redirect('/amadon/checkout')
def clear(request):

    del request.session['list']
    return redirect('/amadon')
def wipe(request):
    request.session.clear()
    return redirect('/amadon')



def handleitems(item_id,quantity):
    print "This is the ID and quantity", item_id, quantity
    if item_id == '1':
        # print "id is 1"
        name = "Coding Dojo Shirt"
        price = 19.99

    elif item_id == '2':
        name = "Coding Dojo Sweater"
        price = 29.99
    elif item_id == '3':
        name = "Coding Dojo Cup"
        price = 4.99
    else:
        name = "Coding Dojo Algorithm Book"
        price = 49.99
    total = price*float(quantity)
    item = [name, price, quantity, total]
    print "THis is in the handler function", item
    return item
