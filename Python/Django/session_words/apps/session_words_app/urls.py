from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^clear$', views.clear),
    url(r'^$', views.index),
    url(r'^process$', views.process),

]
