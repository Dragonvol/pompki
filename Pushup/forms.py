from django import forms
import datetime
from .models import PushUpDay

class AddPushup(forms.ModelForm):
    class Meta:
        model = PushUpDay
        fields = ['count']
        labels = {
            'count':'Ilość pompek'
        }

    def clean(self):
        pass