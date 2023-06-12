from django import forms 
from dashboard.models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','age','height','sex']
        labels = {
            "name":"이름",
            "age":"나이",
            "height":"키",
            "sex":"성별",
        }
