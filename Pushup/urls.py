from django.urls import path
from . import views

app_name = 'pushup'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('home/',views.home_view,name='home'),
    path('add_pushup/',views.add_push_up,name='add_pushup'),
    path('stats/',views.stats_view,name='stats'),
]