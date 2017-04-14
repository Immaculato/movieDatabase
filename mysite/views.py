from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from movies.models import Genre, Movie, Tag, Movie_Has_Tag, Crew, User
from mysite.forms import LoginForm, RegisterForm



def hello(request):
	return HttpResponse("Hello World")

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
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = User.objects.filter(email=form.cleaned_data['email'])
			if not user:
				return HttpResponse("User %s not found"%form.cleaned_data['email'])
			else:
				user = user.filter(password=form.cleaned_data['password'])
				if not user:
					return HttpResponse("Invalid password for user %s!"%form.cleaned_data['email'])
				else:
					user = user.get()
					return HttpResponse("Hello %s!"%user.first_name)
	else:
		form = LoginForm()

	return render(request,'log_in.html', {'form':form})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			login_form = LoginForm(request.POST)
			return render(request,'log_in.html', {'form':login_form})
	else:
		form = RegisterForm()

	return render(request,'register.html', {'form':form})


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
