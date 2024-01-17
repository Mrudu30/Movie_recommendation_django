from django.urls import path
from .views import home,index,mylist,detail,filter_movies
from accounts import views as av
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('home/',home,name='home'),
    path('login/',av.loginaccount,name='login'),
    path('signupaccount/', av.signupaccount, name='signup'),
    path('logout/', av.logoutaccount, name='logout'),
    path('mylist/',mylist,name='mylist'),
    path('<int:movie_id>/', detail, name='detail'),
    path('filter/', filter_movies, name='filter_movies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)