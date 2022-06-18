from django.contrib import admin
from .models import PushUpDay

@admin.register(PushUpDay)
class PushUpAdmin(admin.ModelAdmin):
    list_display = ['user','day','count']


# Register your models here.
