from django import forms
from django.contrib.auth import User
from django.contrib.auth import UserCreationForm

class  UserRegisterForm(UserCreationForm):
    email = forms.emailField()

    class Meta: 
        model = User
        fields =['username','email','password1','password2']