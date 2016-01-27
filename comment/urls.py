from django.conf.urls import url
from . import views
import urllib

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^#about$', views.post_list_about, name='post_list_about'),
    url(r'^#contact$', views.post_list_contact, name='post_list_contact'),
    url(r'^gallery/$', views.gallery, name='gallery'),
]