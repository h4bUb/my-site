import json
import time

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, QueryDict
from django.template import Template, Context, RequestContext
from datetime import datetime
from .models import Counter
from .forms import ContactForm
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
	counter = Counter.objects.get()
	visits = int( request.COOKIES.get('visits', '0') )
	if visits == 1:
		counter.visits += 1
	response =  render(request, 'comment/feed.html', {'visits': counter.visits, 'all_posts': Post.objects.reverse(), 'form': PostForm()})
	if 'last_visit' in request.COOKIES.keys():
		last_visit = request.COOKIES['last_visit']
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
		curr_time = datetime.now()
		if (curr_time-last_visit_time).seconds > 60*10:
			counter.visits = counter.visits + 1
			counter.save()
			response =  render(request, 'comment/feed.html', {'visits': counter.visits, 'all_posts': Post.objects.reverse(), 'form': PostForm()})
			response.set_cookie('visits', visits + 1 )
			response.set_cookie('last_visit', datetime.now())
	else:
		response.set_cookie('last_visit', datetime.now())
	return response

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post', '')
        post_author = request.POST.get('the_author', '')
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

'''
def contact_form(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	if request.POST:
		form = ContactForm(request.POST)
		post = form
		print ('HELLO')
		print ('post.author: ', request.POST.get('name', ''), ' post.text: ', request.POST.get('message', ''))
		if form.is_valid():
			# Only executed with jQuery form request
			if request.is_ajax():
				post = Post()
				post.author = request.POST.get('name', '')
				post.text = request.POST.get('message', '')
				post.published_date = timezone.now()
				post.save()
				return HttpResponse('OK')
			else:
				# render() a form with data (No AJAX)
				# redirect to results ok, or similar may go here
				#post = form.save(commit=False)
				#post.published_date = timezone.now()
				#post.save()
				print ('REDIRECTING')
				return redirect('blog.views.post_detail', pk=post.pk)
		else:
			if request.is_ajax():
				# Prepare JSON for parsing
				errors_dict = {}
				if form.errors:
					for error in form.errors:
						e = form.errors[error]
						errors_dict[error] = str(e)
				return HttpResponseBadRequest(json.dumps(errors_dict))
			else:
				# render() form with errors (No AJAX)
				pass
	else:
		form = ContactForm()
	return render(request, 'comment/form.html', {'form': form, 'posts': posts})
'''

def index(request):
	#print ('cookie: ', request.COOKIES.get('visits', '0'))
	counter = get_object_or_404(Counter)
	#print ('counter.visits: ', counter.visits)
	visits = int( request.COOKIES.get('visits', '0') )
	#print ("visits: ", visits)
	if visits == 1:
	    counter.visits += 1
	response =  render(request, 'comment/index.html', {'visits': counter.visits})
	if 'last_visit' in request.COOKIES.keys():
		last_visit = request.COOKIES['last_visit']
		#print ('last_visit: ', last_visit)
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
		#print ('last_visit_time: ', last_visit_time)
		curr_time = datetime.now()
		#print ('curr_time: ', curr_time, ' minus: ', (curr_time-last_visit_time).seconds)
		if (curr_time-last_visit_time).seconds > 60*10:
			#ALLVISITORS = ALLVISITORS + 1
			#print ('old counter.visits: ', counter.visits)
			counter.visits = counter.visits + 1
			counter.save()
			#print ('changing visits: ', visits + 1)
			#print ('changing counter.visits: ', counter.visits)
			response =  render(request, 'comment/index.html', {'visits': counter.visits})
			response.set_cookie('visits', visits + 1 )
			response.set_cookie('last_visit', datetime.now())
	else:
		response.set_cookie('last_visit', datetime.now())
	return response

def gallery(request):
	counter = Counter.objects.get()
	visits = int( request.COOKIES.get('visits', '0') )
	if visits == 1:
	    counter.visits += 1
	response =  render(request, 'comment/gallery.html', {'visits': counter.visits})
	if 'last_visit' in request.COOKIES.keys():
		last_visit = request.COOKIES['last_visit']
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
		curr_time = datetime.now()
		if (curr_time-last_visit_time).seconds > 60*10:
			counter.visits = counter.visits + 1
			counter.save()
			response =  render(request, 'comment/gallery.html', {'visits': counter.visits})
			response.set_cookie('visits', visits + 1 )
			response.set_cookie('last_visit', datetime.now())
	else:
		response.set_cookie('last_visit', datetime.now())
	return response