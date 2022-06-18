from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label ='Hasło',widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,required=True,label = "Nazwa użytkownika")
    password1 = forms.CharField(label='Hasło',strip=False,widget=forms.PasswordInput())
    password2 = forms.CharField(label='Potwierdź hasło',strip=False,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username","password1","password2"]