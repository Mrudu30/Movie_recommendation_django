from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class userCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
    
        model = User
        fields = ['username','email', 'password1', 'password2']