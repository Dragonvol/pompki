from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import date,timedelta

class PushUpDay(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    day = models.DateField(default= timezone.now())
    count = models.IntegerField(null=False,validators=[
        MinValueValidator(1),
        MaxValueValidator(10000)
    ])

def top5_this_week():
    class pushup:
        def __init__(self,user):
            self.user=user
        total_count = 0
    users= User.objects.all()
    pushups_obj = []
    for user in users:
        pushups_obj.append(pushup(user))
    pushups = PushUpDay.objects.filter(day__gte=date.today() - timedelta(days=7))
    for pushup in pushups_obj:
        for p in pushups:
            if pushup.user == p.user:
                pushup.total_count+=p.count
    return sorted(pushups_obj,reverse=True,key=lambda x:x.total_count)[:5]

def top3_this_month():
    class seria:
        def __init__(self,user):
            self.user = user
        series = 0

    users = User.objects.all()
    series_obj = []
    for user in users:
        series_obj.append(seria(user))
    pushups = PushUpDay.objects.filter(day__gte=date.today()-timedelta(days=30))
    for series in series_obj:
        for p in pushups:
            if series.user == p.user:
                series.series+=1
    return sorted(series_obj,reverse=True,key=lambda x:x.series)[:3]

