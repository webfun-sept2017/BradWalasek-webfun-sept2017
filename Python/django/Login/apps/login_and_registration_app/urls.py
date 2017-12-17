from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^clear$', views.clear),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^$', views.index),
]
