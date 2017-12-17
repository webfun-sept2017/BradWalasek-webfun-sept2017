from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^process$', views.process),
    url(r'^result$', views.result),
    url(r'^$', views.index),
]
