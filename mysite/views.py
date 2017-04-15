from django.shortcuts import render, redirect
from django.http import HttpResponse  
import datetime
from movies.models import *
from mysite.forms import *

def hello(request):
	return HttpResponse("Hello world")

def homepage(request):
	return HttpResponse("CS405 Homepage")

def home_page(request):
	return render(request, 'home_page.html')

def log_in(request):
	if 'email' in request.session:
		log_out_link = '<br /><a href="/logout/">Click here to log out.</a>'
		return HttpResponse("Already logged in with email %s%s"%(request.session['email'],log_out_link))
	else:
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
						request.session['email'] = user.email
						response_string = "Hello %s!"%user.first_name
						if user.manager:
						    request.session['manager'] = True
						    response_string += " You are a manager."
						elif 'manager' in request.session:
						    # If prviously logged in as manager,
						    # need to delete key and mark as modified
						    del request.session['manager']
						    request.session.modified = True
						# Cookies will expire when browser closes
						request.session.set_expiry(0)
						return HttpResponse(response_string)
		else:
        		form = LoginForm();
		return render(request,'log_in.html', {'form':form})

def log_out(request):
	if 'manager' in request.session:
		del request.session['manager']
	if 'email' in request.session:
		del request.session['email']
	request.session.modified = True
	return redirect('/login/',request)

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

def is_manager(request):
	return 'manager' in request.session
def must_be_manager_response():
	return HttpResponse('Must be logged in as a manager to complete this function')

def edit_crew(request):
	if is_manager(request):
		if request.method == 'POST':
			crew_form = CrewForm(request.POST);
			if crew_form.is_valid():
				crew_form.save()
			else:
				return HttpResponse('Invalid form input')
		else:
			crew_form = CrewForm();

		return render(request,'edit_crew.html',{'crew_form':crew_form})
	else:
		return HttpResponse('Must be logged in as a manager to edit crew')

def disable_empty_checks(form):
	for field in form.fields:
	    form.fields[field].required = False

def force_empty_checks(form,except_for=[]):
	for field in form.fields:
		if field not in except_for:
			form.fields[field].required = True

def edit_movie(request):
	if is_manager(request):
		if request.method == 'POST':
			movie_form = MovieForm(request.POST)
			if request.POST['action'] == 'Submit Movie':
				genre_form = GenreForm()
				disable_empty_checks(genre_form)
				tag_form = TagForm()
				disable_empty_checks(tag_form)
				force_empty_checks(movie_form,'tag')
				if movie_form.is_valid():
					new_movie = movie_form.save()
					return redirect('/movie/?id=%s'%new_movie.id, request)

			elif request.POST['action'] == 'Add Tag': 
				disable_empty_checks(movie_form)
				genre_form = GenreForm(request.POST)
				disable_empty_checks(genre_form)
				tag_form = TagForm(request.POST)
				force_empty_checks(tag_form)
				if tag_form.is_valid():
					tag_form.save()
					tag_form=TagForm()
					disable_empty_checks(tag_form)

			elif request.POST['action'] == 'Add Genre': 
				disable_empty_checks(movie_form)
				tag_form  = GenreForm(request.POST)
				disable_empty_checks(tag_form)
				genre_form = GenreForm(request.POST)
				force_empty_checks(genre_form)
				if genre_form.is_valid():
					genre_form.save()
					genre_form=GenreForm()
					disable_empty_checks(genre_form)
		else:
			genre_form = GenreForm()
			movie_form = MovieForm()
			tag_form   = TagForm()
			disable_empty_checks(movie_form)
			disable_empty_checks(genre_form)
			disable_empty_checks(tag_form  )

		return render(request,'edit_movie.html',{'movie_form':movie_form,'genre_form':genre_form,'tag_form':tag_form})
	else:
		return HttpResponse('Must be logged in as a manager to edit movies')

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

def promote(request):
	if is_manager(request):
		if request.method == "POST":
			if 'to_be_promoted' in request.POST:
				new_manager_emails = request.POST.getlist('to_be_promoted')
				for email in new_manager_emails:
					new_manager = User.objects.get(email=email)
					new_manager.manager = True
					new_manager.save()
				return HttpResponse('Successfully promoted %s'%', '.join(new_manager_emails))
		else:
			normal_users = User.objects.filter(manager=False)
			return render(request, 'promote.html',{'users':normal_users})
	else:
		return HttpResponse('Must be logged in as a manager to edit crew')

def movies_by_genres(request):
	if 'g_id' in request.GET:
		ID = request.GET['g_id']
		results = Movie.objects.filter(genre__id=ID)
		return render(request, 'movies_by_genre.html',
                             {'movies': results, 'ID': ID})
