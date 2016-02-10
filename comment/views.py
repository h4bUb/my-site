import json
import time

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, QueryDict
from django.template import Template, Context, RequestContext
from datetime import datetime
from .models import Counter
from .forms import ContactForm
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import Ip
from django.utils.html import strip_tags


def post_list(request):
    counter = get_object_or_404(Counter)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    #print ('ip: ', ip)
    add = True
    for i in Ip.objects.all():
        print (i.ip_address)
        if ip == i.ip_address:
            add = False
            break
    if add:
        get_ip= Ip()
        get_ip.ip_address= ip
        get_ip.save()
        counter.visits += 1
        counter.save()
        #print ("added")

    visits = int( request.COOKIES.get('visits', '0') )
    response =  render(request, 'comment/feed.html', {'visits': counter.visits, 'all_posts': Post.objects.reverse(), 'form': PostForm()})
    if 'last_visit' in request.COOKIES.keys():
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        curr_time = datetime.now()
        if (curr_time-last_visit_time).seconds > 600:
            if not add:
                counter.visits += 1
                counter.save()
                response =  render(request, 'comment/feed.html', {'visits': counter.visits})
            response.set_cookie('visits', visits + 1 )
            response.set_cookie('last_visit', datetime.now())
    else:
        if not add:
            counter.visits += 1
            counter.save()
            response = render(request, 'comment/feed.html', {'visits': counter.visits})
        response.set_cookie('last_visit', datetime.now())
    return response

def create_post(request):
    if request.method == 'POST':
        post_text = strip_tags(request.POST.get('the_post', ''))
        post_author = strip_tags(request.POST.get('the_author', ''))
        response_data = {}

        post = Post(text=post_text, author=post_author)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"None": "None"}),
            content_type="application/json"
        )

def index(request):
    #print ('cookie: ', request.COOKIES.get('visits'))
    counter = get_object_or_404(Counter)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    #print ('ip: ', ip)
    add = True
    for i in Ip.objects.all():
        print (i.ip_address)
        if ip == i.ip_address:
            add = False
            break
    if add:
        get_ip= Ip()
        get_ip.ip_address= ip
        get_ip.save()
        counter.visits += 1
        counter.save()
        #print ("added")

    #print ('counter.visits: ', counter.visits)
    visits = int( request.COOKIES.get('visits', '0') )
    response = render(request, 'comment/index.html', {'visits': counter.visits})
    if 'last_visit' in request.COOKIES.keys():
        last_visit = request.COOKIES['last_visit']
        #print ('last_visit: ', last_visit)
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        #print ('last_visit_time: ', last_visit_time)
        curr_time = datetime.now()
        #print ('curr_time: ', curr_time, ' minus: ', (curr_time-last_visit_time).seconds)
        if (curr_time-last_visit_time).seconds > 600:
            #ALLVISITORS = ALLVISITORS + 1
            #print ('old counter.visits: ', counter.visits)
            if not add:
                counter.visits += 1
                counter.save()
                response =  render(request, 'comment/index.html', {'visits': counter.visits})
            #print ('changing visits: ', visits + 1)
            #print ('changing counter.visits: ', counter.visits)
            response.set_cookie('visits', visits + 1 )
            response.set_cookie('last_visit', datetime.now())
    else:
        if not add:
            counter.visits += 1
            counter.save()
            response =  render(request, 'comment/index.html', {'visits': counter.visits})
        response.set_cookie('last_visit', datetime.now())
    return response

def gallery(request):
    counter = get_object_or_404(Counter)

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    #print ('ip: ', ip)
    add = True
    for i in Ip.objects.all():
        print (i.ip_address)
        if ip == i.ip_address:
            add = False
            break
    if add:
        get_ip= Ip()
        get_ip.ip_address= ip
        get_ip.save()
        counter.visits += 1
        counter.save()
        #print ("added")

    visits = int( request.COOKIES.get('visits', '0') )
    response =  render(request, 'comment/gallery.html', {'visits': counter.visits})
    if 'last_visit' in request.COOKIES.keys():
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        curr_time = datetime.now()
        if (curr_time-last_visit_time).seconds > 600:
            if not add:
                counter.visits += 1
                counter.save()
                response =  render(request, 'comment/gallery.html', {'visits': counter.visits})
            response.set_cookie('visits', visits + 1 )
            response.set_cookie('last_visit', datetime.now())
    else:
        if not add:
            counter.visits += 1
            counter.save()
            response =  render(request, 'comment/gallery.html', {'visits': counter.visits})
        response.set_cookie('last_visit', datetime.now())
    return response