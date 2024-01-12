from django import forms
from .models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'contact_no', 'address', 'gender']

        widgets = {
            'password': forms.PasswordInput(),
        }