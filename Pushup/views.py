from django.shortcuts import render
from .forms import AddPushup
from .models import PushUpDay,top5_this_week,top3_this_month
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def home_view(request):
    return render(request,'home.html',{})

@login_required(login_url='/login')
def add_push_up(request):
    push_ups = PushUpDay.objects.filter(user=request.user,day=timezone.now())
    if push_ups:
        msg = 'Dzisiaj już dodałeś pompki, poczekaj do jutra'
    else:
        msg=None
    if request.method=="POST":
        form = AddPushup(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect('/home')
    else:
        form = AddPushup()
    return render(request,'pushup/add_pushup.html',{'form':form,'msg':msg})

def stats_view(request):
    top5 = top5_this_week()
    top3 = top3_this_month()
    return render(request,'pushup/stats.html',{
        'top5':top5,
        'top3':top3
    })