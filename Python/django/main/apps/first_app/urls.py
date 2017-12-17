from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^test$', views.test),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<word>\w+)$',views.show_word),
    url(r'^(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.month_archive)
]
