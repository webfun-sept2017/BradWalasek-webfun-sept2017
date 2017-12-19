from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^show/(?P<number>\d+)', views.show),
    url(r'^clear$', views.clear),
    url(r'^show$', views.show),
    url(r'^create$', views.create),
    url(r'^new$', views.new),
    url(r'^$', views.index),
]
