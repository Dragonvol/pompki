from .forms import RegisterForm
from Pushup.models import Profile
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
            user.profile.name=form.cleaned_data.get('name')
            user.profile.surname=form.cleaned_data.get('surname')
            user.profile.age=form.cleaned_data.get('age')
            user.profile.save()
            user.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html',{'form':form})

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()