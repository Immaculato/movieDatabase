from django.shortcuts import render
from django.http import HttpResponse  
import datetime
from movies.models import Genre, Movie, Tag, Movie_Has_Tag, Crew





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
                    crew_first_name = Crew.objects.filter(c_first_name__icontains=q)
                    return render(request, 'search_results.html',
                                  {'crews': crew_first_name, 'query': q})
        return render(request, 'search_form.html', {'errors': errors})


def movie(request):

        if 'id' in request.GET:
                ID = request.GET['id']
                results = Movie.objects.get(pk = ID)
                return render(request, 'movie_info.html',
                             {'movie': results, 'ID': ID})


def movies_by_genres(request):
        if 'g_id' in request.GET:
                ID = request.GET['g_id']
                results = Movie.objects.filter(genre__id=ID)
                return render(request, 'movies_by_genre.html',
                             {'movies': results, 'ID': ID})
