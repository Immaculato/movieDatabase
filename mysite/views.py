from django.shortcuts import render
from django.http import HttpResponse  
import datetime
from movies.models import Genre, Movie, Tag, Movie_Has_Tag, Crew



def hello(request):
	return HttpResponse("Hello world")

def homepage(request):
	return HttpResponse("CS405 Homepage")

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_date.html', {'current_date': now,
						     'u_fname': 'Mark',
						     'u_mname': 'Daniel',
						     'u_lname': 'Ng' })

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "In %s hour(s), it will be %s." % (offset, dt)
	return HttpResponse(html)


def home_page(request):
	return render(request, 'home_page.html')

def log_in(request):
	return render(request, 'log_in.html')

def get_log_in_info(request):
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = log_in_form(request.POST)
	# check whether it's valid:
		if form.is_valid():
	# process the data in form.cleaned_data as required
	# ...
	# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = log_in_form()

	return render(request, 'log_in.html', {'form': form})



def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
		    errors.append('Enter a search term.')
		elif len(q) > 15:
		    errors.append('Please enter at most 15 characters.')
		else:
		    genres = Genre.objects.filter(g_name__icontains=q)
		    return render(request, 'search_results.html',
				  {'genres': genres, 'query': q})
	return render(request, 'search_form.html', {'errors': errors})



