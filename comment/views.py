from django.shortcuts import render
#from django.utils.http import urlencode
from django.utils.encoding import iri_to_uri
from django.utils.html import escape

def post_list(request):
    return render(request, 'comment/index.html', {})

def post_list_about(request):
    return render(request, escape(iri_to_uri(u"comment/index.html#about")), {})

def post_list_contact(request):
    return render(request, escape(iri_to_uri(u"comment/index.html#contact")), {})

def gallery(request):
    return render(request, 'comment/gallery.html', {})