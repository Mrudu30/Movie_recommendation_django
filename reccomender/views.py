from django.shortcuts import redirect,render,get_object_or_404
from django.db.models import Q
from .models import Movie,MyList,Genre,Language
from django.contrib import messages
from django.http import Http404
from .forms import GenreFilterForm,LanguageFilterForm

def home(request):
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(Q(
            name__icontains=query)).distinct()
        context =  {'movies': movies}
    else:
        movies = Movie.objects.all()
        context =  {'movies': movies}
    
    return render(request,'home.html',context)

def detail(request,movie_id):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    movies = get_object_or_404(Movie, id=movie_id)
    movie = Movie.objects.get(id=movie_id)
    
    temp = list(MyList.objects.all().values().filter(movie_id=movie_id,user=request.user))
    if temp:
        update = temp[0]['watch']
    else:
        update = False
    if request.method == "POST":

        # For my list
        if 'watch' in request.POST:
            watch_flag = request.POST['watch']
            if watch_flag == 'on':
                update = True
            else:
                update = False
        if MyList.objects.all().values().filter(movie_id=movie_id,user=request.user):
            MyList.objects.all().values().filter(movie_id=movie_id,user=request.user).update(watch=update)
        else:
            MyList(user=request.user,movie=movie,watch=update).save()
        if update:
            messages.success(request, "Movie added to your list!")
        else:
            messages.success(request, "Movie removed from your list!")
    context = {'movies': movies,'update':update}
    return render(request, 'detail.html', context)

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
        return render(request, 'filtered_movies_result.html', {'movies': movies})

    return render(request, 'filtered_movies.html', {'movies': movies, 'genre_form': genre_form, 'language_form': language_form})


def index(request):
    return render(request,'index.html')

def mylist(request):

    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404

    movies = Movie.objects.filter(mylist__watch=True,mylist__user=request.user)
   
    return render(request, 'mylist.html', {'movies': movies})