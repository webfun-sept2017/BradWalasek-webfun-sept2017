from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book/(?P<string>\w+)', views.showbook),
    url(r'^book/add', views.add),
    url(r'^book', views.show),
    url(r'^logout', views.logout),
    url(r'^login', views.login),
    url(r'^clear', views.clear),
    url(r'^create', views.create),
    url(r'^', views.index)
]
