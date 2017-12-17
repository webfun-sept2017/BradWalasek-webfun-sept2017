from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<number>\d+)/update$', views.update),
    url(r'^create$', views.create),
    url(r'^new$', views.new),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/destroy$', views.destroy),
    url(r'^$', views.index)
]
