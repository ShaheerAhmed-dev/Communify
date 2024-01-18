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
        fields = ['text', 'image', 'private', 'type']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),  # Add any additional attributes or classes you want
        }

# class PostTypeForm(forms.Form):
#     class Meta:
#         model = PostType
#         fields = 'type_name'       

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Assuming your Comment model has a ForeignKey to the User model
            self.fields['name'].widget = forms.Select(choices=CustomUser.objects.all().values_list('id', 'username'))