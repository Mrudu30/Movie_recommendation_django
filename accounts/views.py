from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .forms import UserCreationForm,AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here
# reset password 
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')

# sign up / new user
def signupaccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = request.POST['email']
            user.save()
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    else:
        form = UserCreationForm()
    return render(request, 'signupaccount.html', {'form': form})
       
       
# logout account
def logoutaccount(request):        
    logout(request)
    return redirect('home')

# login account
def loginaccount(request):    
    if request.method == 'GET':
        return render(request, 'loginaccount.html', 
                      {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html', 
                    {'form': AuthenticationForm(), 
                    'error': 'username and password do not match'})
        else: 
            login(request,user)
            return redirect('home')