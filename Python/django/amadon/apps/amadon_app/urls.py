from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'checkout$', views.checkout),
    url(r'basket$', views.basket),
    url(r'buy$', views.purchase),
    url(r'clear$', views.clear),
    url(r'wipe$', views.wipe),
    url(r'^', views.index),
]
