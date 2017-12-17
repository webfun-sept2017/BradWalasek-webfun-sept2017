from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'refresh$', views.refresh),
    url(r'process_money$', views.process),
    url(r'^$', views.index),
]
