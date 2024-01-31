from django import forms
from .models import CustomUser, Post, Profile, Like, Share
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
# from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        email = forms.EmailField()
        fields = ['username', 'email']



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



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'post', 'user']

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['post', 'from_user', 'to_user']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Assuming your Comment model has a ForeignKey to the User model
            self.fields['to_user'].widget = forms.ChoiceField(choices=CustomUser)

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['user', 'post']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Assuming your Comment model has a ForeignKey to the User model
    #     self.fields['name'].widget = forms.Select(choices=CustomUser.objects.all().values_list('id', 'username'))

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'about_me']