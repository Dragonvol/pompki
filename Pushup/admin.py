from django.contrib import admin
from .models import PushUpDay,Profile

@admin.register(PushUpDay)
class PushUpAdmin(admin.ModelAdmin):
    list_display = ['user','day','count']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','surname','age']
# Register your models here.
