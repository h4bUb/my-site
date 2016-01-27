from django.shortcuts import render
import urllib

def post_list(request):
    return render(request, 'comment/index.html', {})

def post_list_about(request):
    return render(request, urllib.urlencode(r'comment/index.html#about'), {})

def post_list_contact(request):
    return render(request, urllib.urlencode(r'comment/index.html#contact'), {})

def gallery(request):
    return render(request, 'comment/gallery.html', {})