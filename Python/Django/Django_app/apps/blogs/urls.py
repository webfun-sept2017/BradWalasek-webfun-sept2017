from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^new', views.new),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/update$', views.update),
    url(r'^(?P<number>\d+)/destroy$', views.destroy),
    url(r'create$', views.create),
]
