from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label ='Hasło',widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,required=True,label = "Nazwa użytkownika/pseudonim")
    name = forms.CharField(max_length=30,required=True,label='Imię')
    surname = forms.CharField(max_length=30,required=True,label='Nazwisko')
    age = forms.IntegerField(required=True,validators=[
        MinValueValidator(10),
        MaxValueValidator(90)
    ])
    password1 = forms.CharField(label='Hasło',strip=False,widget=forms.PasswordInput())
    password2 = forms.CharField(label='Potwierdź hasło',strip=False,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username",'name','surname','age',"password1","password2"]