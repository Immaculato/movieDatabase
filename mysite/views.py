from django.shortcuts import render, redirect
from django.http import HttpResponse  
import datetime
from movies.models import Genre, Movie, Tag, Movie_Has_Tag, Crew, User
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
	if 'search_type' in request.GET:
		search_type = request.GET['search_type']
		if (search_type == "Title"):
			option = 1
		elif (search_type == "Genre"):
			option = 2
		elif (search_type == "Tag"):
			option = 3
		elif (search_type == "Crew"):
			option = 4
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
		    errors.append('Enter a search term.')
		elif len(q) > 15:
		    errors.append('Please enter at most 15 characters.')
		elif option == 1:
		    m_title = Movie.objects.filter(title__icontains=q)
		    return render(request, 'search_results.html',
				  {'movies': m_title, 'query': q})
		elif option == 2:
		    genres = Genre.objects.filter(g_name__icontains=q)
		    return render(request, 'search_results.html',
				  {'genres': genres, 'query': q})
		elif option == 3:
		    tags = Tag.objects.filter(t_name__icontains=q)
		    return render(request, 'search_results.html',
				  {'tags': tags, 'query': q})
		elif option == 4:
		    crew_first_name = Crew.objects.filter(crew_first_name__icontains=q)
		    return render(request, 'search_results.html',
				  {'crews': crew_first_name, 'query': q})
	return render(request, 'search_form.html', {'errors': errors})


def movie(request):

	if 'id' in request.GET:
		ID = request.GET['id']
		results = Movie.objects.get(pk = ID)
		genre = Genre.objects.filter(movie__id=ID)
		return render(request, 'movie_info.html',
                             {'movie': results, 'genre': genre, 'ID': ID})


def movies_by_genres(request):
	if 'g_id' in request.GET:
		ID = request.GET['g_id']
		results = Movie.objects.filter(genre__id=ID)
		return render(request, 'movies_by_genre.html',
                             {'movies': results, 'ID': ID})
