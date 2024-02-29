from django.urls import path
from .views import home,index,mylist,detail,filter_movies,deleteComment,editComment
from accounts import views as av
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',index),
    path('password-reset/',av.ResetPasswordView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('login/',av.loginaccount,name='login'),
    path('signupaccount/', av.signupaccount, name='signup'),
    path('logout/', av.logoutaccount, name='logout'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('home/',home,name='home'),
    path('mylist/',mylist,name='mylist'),
    path('detail/<int:movie_id>/', detail, name='detail'),
    path('filter/', filter_movies, name='filter_movies'),
    path('delete-comment/<str:id>/',deleteComment,name="delete_comment"),
    path('editComment/<str:id>/',editComment,name="edit_comment"),
]

handler404 = 'reccomender.views.page_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)