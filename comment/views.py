from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from datetime import datetime
from .models import Counter


def post_list(request):
	#print ('cookie: ', request.COOKIES.get('visits', '0'))
	counter = Counter.objects.get()
	#print ('counter.visits: ', counter.visits)
	visits = int( request.COOKIES.get('visits', '0') )
	#print ("visits: ", visits)
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