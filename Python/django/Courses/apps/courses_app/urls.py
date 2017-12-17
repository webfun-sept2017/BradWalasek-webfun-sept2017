from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<var>\d+)/destroy', views.destroy),
    url(r'^(?P<var>\d+)/remove', views.remove),
    url(r'^create', views.create),
    url(r'^$', views.index),
]
