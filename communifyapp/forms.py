from django import forms
from .models import UserModel, Post


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'contact_no', 'address', 'gender']

        widgets = {
            'password': forms.PasswordInput(),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'private']        