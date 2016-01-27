from django.shortcuts import render
#from .models import Post

def post_list(request):
    return render(request, 'comment/index.html', {})

def post_list_about(request):
    return render(request, 'comment/index.html#about', {})

def post_list_contact(request):
    return render(request, 'comment/index.html#contact', {})

def gallery(request):
    return render(request, 'comment/gallery.html', {})