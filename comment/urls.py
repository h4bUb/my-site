from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^gallery/$', views.gallery, name='gallery'),
	url(r'^feedback/$', views.post_list, name='post_list'),
    url(r'^feedback/create_post/$', views.create_post, name='create_post'),
	#url(r'^form/$', views.contact_form, name="contact_form"),
]