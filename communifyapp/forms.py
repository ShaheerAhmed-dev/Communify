from django import forms
from .models import CustomUser, Post
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        email = forms.EmailField()
        fields = ['username', 'email', 'password']


        widgets = {
            'password': forms.PasswordInput(),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image', 'private']        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)

