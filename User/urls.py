from django.urls import path
from . import views
from django.contrib.auth import views as v
from .forms import UserLoginForm

app_name='user'

urlpatterns = [
    path('register/',views.sign_up,name='register'),
    path('login/',v.LoginView.as_view(template_name="registration/login.html",authentication_form=UserLoginForm),
         name = 'login'),
]