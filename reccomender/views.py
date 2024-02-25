from django.shortcuts import redirect,render,get_object_or_404
from django.db.models import Q
from .models import Movie,MyList
from django.contrib import messages
from django.http import Http404
from .forms import GenreFilterForm,LanguageFilterForm
import time

# video page
def index(request):
    return render(request,'index.html')

# user specific mylist
def mylist(request):

    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404

    movies = Movie.objects.filter(mylist__watch=True,mylist__user=request.user)
   
    return render(request, 'initTemplates/mylist.html', {'movies': movies})

# home page
def home(request):
    query = request.POST.get('q')
    if query:
        movies = Movie.objects.filter(Q(
            name__icontains=query)).distinct()
        context =  {'movies': movies}
        return render(request,'initTemplates/search.html',context)
    else:
        movies = Movie.objects.all()
        context =  {'movies': movies}
    
    return render(request,'initTemplates/home.html',context)

# detail page
def detail(request, movie_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_active:
        raise Http404

    movie = get_object_or_404(Movie, id=movie_id)
    is_in_my_list = MyList.objects.filter(user=request.user, movie=movie).exists()

    if request.method == 'POST':
        watch_flag = request.POST.get('watch', False)
        if watch_flag == 'on':
            if not is_in_my_list:
                # Add movie to user's list
                MyList.objects.create(user=request.user, movie=movie)
                messages.success(request, f'{movie.name} added to your list.')

            if is_in_my_list:
                # Remove movie from user's list
                MyList.objects.filter(user=request.user, movie=movie).delete()
                messages.success(request, f'{movie.name} removed from your list.')
                time.sleep(2)
                return redirect('mylist')

        # Redirect back to the movie detail page
        return redirect('detail', movie_id=movie_id)

    context = {'movie': movie, 'is_in_my_list': is_in_my_list}
    return render(request, 'initTemplates/detail.html', context)

# recomendation system
def filter_movies(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    
    genre_form = GenreFilterForm(request.GET)
    language_form = LanguageFilterForm(request.GET)
    movies = Movie.objects.all()

    if genre_form.is_valid() and language_form.is_valid():
        selected_genre = genre_form.cleaned_data['genre']
        selected_languages = language_form.cleaned_data['languages']

        if selected_genre:
            genre_filter = Q(genre__in=selected_genre)
        else:
            genre_filter = Q()

        if selected_languages:
            language_filter = Q(languages__in=selected_languages)
        else:
            language_filter = Q()

        movies = movies.filter(genre_filter & language_filter).distinct()
        # Redirect to the result page with filtered movies
        return render(request, 'filter/filtered_movies_result.html', {'movies': movies})

    return render(request, 'filter/filtered_movies.html', {'movies': movies, 'genre_form': genre_form, 'language_form': language_form})

# 404 page
def page_404(request,execption):   
    return render(request, 'errorpages/404_page.html', status=404)