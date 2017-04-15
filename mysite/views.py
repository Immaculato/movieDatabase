from django.shortcuts import render, redirect
from django.http import HttpResponse  
import datetime
from movies.models import *
from mysite.forms import LoginForm, RegisterForm, MovieForm, CrewForm

def hello(request):
	return HttpResponse("Hello world")

def homepage(request):
	return HttpResponse("CS405 Homepage")

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
        	form = LoginForm();
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

def edit_crew(request):
	if request.method == 'POST':
		crew_form = CrewForm(request.POST);
		if crew_form.is_valid():
			crew_form.save()
		else:
			return HttpResponse('Invalid form input')
	else:
		crew_form = CrewForm();

	return render(request,'edit_crew.html',{'crew_form':crew_form})

def edit_movie(request):
	if request.method == 'POST':
		form = MovieForm(request.POST);
	else:
		form = MovieForm();

	return render(request,'edit_movie.html',{'form':form})

	
	

def search(request):
	errors = []
	g_ids = []
	if 'Search' in request.GET:

		movies = Movie.objects.all()
		if 'g_id' in request.GET:
			g_ids = request.GET.getlist('g_id')
			if g_ids:
				movies = movies.filter(genre__id__in=g_ids)
		if 'tag_q' in request.GET:
			tag_q = request.GET['tag_q']
			if tag_q:
				movies = movies.filter(tag__t_name__icontains=tag_q)
		if 'crew_q' in request.GET:
			crew_q = request.GET['crew_q']
			if crew_q:
				movies = movies.filter(crew__crew_first_name__icontains=crew_q)
		if 'crew_q2' in request.GET:
			crew_q2 = request.GET['crew_q2']
			if crew_q2:
				movies = movies.filter(crew__crew_last_name__icontains=crew_q2)
		if 'title_q' in request.GET:
			title_q = request.GET['title_q']
			if title_q:
				movies = movies.filter(title__icontains=title_q)
		return render(request, 'search_results.html', {'genre': Genre.objects.filter(id__in=g_ids), 
								'tag': tag_q,
								'crew': crew_q,
								'title': title_q,
								'movies': movies.distinct, })

	else:

		genres = Genre.objects.all()	
		return render(request, 'search_form.html', {'errors': errors,
							    'genres': genres,})


def movie(request):

	if 'id' in request.GET:
		ID = request.GET['id']
		results = Movie.objects.get(pk = ID)
		genre = Genre.objects.filter(movie__id=ID)
		tags = Tag.objects.filter(movie__id=ID)
		crew = Crew.objects.filter(m_id=ID)
		print(crew)
		review = Review.objects.filter(movie__id=ID)
		return render(request, 'movie_info.html',
                             {'movie': results, 'genre': genre,
			      'tags': tags, 'crew': crew, 'ID': ID,
			      'reviews': review})


def movies_by_genres(request):
	if 'g_id' in request.GET:
		ID = request.GET['g_id']
		results = Movie.objects.filter(genre__id=ID)
		return render(request, 'movies_by_genre.html',
                             {'movies': results, 'ID': ID})
