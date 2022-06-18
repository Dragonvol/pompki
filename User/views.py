from .forms import RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models.signals import post_save
from django.dispatch import receiver


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html',{'form':form})