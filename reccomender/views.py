from django.shortcuts import redirect,render,get_object_or_404
from django.db.models import Q
from .models import Movie,MyList,Comments
from django.contrib import messages
from django.http import Http404,JsonResponse
from .forms import GenreFilterForm,LanguageFilterForm

# video page
def index(request):
    return render(request,'index.html')

# user specific mylist
def mylist(request):

    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        return render(request, 'errorpages/404_page.html', status=404)

    query = request.POST.get('q')
    if query:
        movies = Movie.objects.filter(Q(
            name__icontains=query)).distinct()
        context =  {'movies': movies}
        return render(request,'initTemplates/search.html',context)

    movies = Movie.objects.filter(mylist__user=request.user)
    return render(request, 'initTemplates/mylist.html', {'movies': movies})

# home page
def home(request):
    query = request.POST.get('q')
    if query:
        movies = Movie.objects.filter(Q(
            name__icontains=query)).distinct()
        context =  {'movies': movies}
        return render(request,'initTemplates/search.html',context)

    latest_movies = Movie.objects.order_by('-date_of_release')[:10]
    comedy_movies = Movie.objects.filter(genre__name='Comedy').order_by('-date_of_release')
    movies = Movie.objects.all()
    context =  {'movies': movies,'latest_movies':latest_movies,'comedy_movies':comedy_movies}
    
    return render(request,'initTemplates/home.html',context)

# detail page
def detail(request, movie_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    query = request.POST.get('q')
    if query:
        movies = Movie.objects.filter(Q(
            name__icontains=query)).distinct()
        context =  {'movies': movies}
        return render(request,'initTemplates/search.html',context)

    if not request.user.is_active:
        return render(request, 'errorpages/404_page.html', status=404)
    
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        newcomment = request.POST.get('newcomment')
        if newcomment:
            commentuser = request.user
            commentmovie = movie
            Comments.objects.create(user=commentuser,movie=commentmovie,comment=newcomment)
        
    is_in_my_list = MyList.objects.filter(user=request.user, movie=movie).exists()
    comments = Comments.objects.filter(movie=movie)
    
    if request.method == 'POST':
        watch_flag = request.POST.get('watch', False)
        watch_flag = watch_flag == 'on' 
        if watch_flag:
            my_list, created = MyList.objects.get_or_create(user=request.user, movie=movie)
            if created:
                messages.success(request, f'{movie.name} added to your list.')
            else:
                my_list.delete()
                messages.success(request, f'{movie.name} removed from your list.')
            return redirect('detail', movie_id=movie_id)
        return redirect('detail', movie_id=movie_id)

    context = {'movie': movie, 'is_in_my_list': is_in_my_list,'comments':comments}
    return render(request, 'initTemplates/detail.html', context)

# comment edit and delete
def editComment(request,id):
    comment = get_object_or_404(Comments, id=id)
    if request.method == 'POST':
        editedComment = request.POST.get('editedComment')
        comment.comment = editedComment
        comment.save()
        return JsonResponse({"status":"success"})
    else:
        return JsonResponse({"status":"error"})

def deleteComment(request,id):
    comment = get_object_or_404(Comments, id=id)
    
    if request.method == 'POST':
        comment.delete()
        return JsonResponse({"status":"success"})

# recomendation system
def filter_movies(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        return render(request, 'errorpages/404_page.html', status=404)
    
    query = request.POST.get('q')
    if query:
        movies = Movie.objects.filter(Q(
            name__icontains=query)).distinct()
        context =  {'movies': movies}
        return render(request,'initTemplates/search.html',context)
    
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
def page_404(request,exception):   
    return render(request, 'errorpages/404_page.html', status=404)