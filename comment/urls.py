from django.conf.urls import url, include
from . import views
import urllib

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^index/$', views.post_list, name='post_list'),
    url(r'^gallery/$', views.gallery, name='gallery'),
]