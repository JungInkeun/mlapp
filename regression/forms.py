from django import forms
from regression.models import BikeData

class BikeDataForm(forms.ModelForm):
    class Meta:
        model = BikeData
        fields = ['season','workingday', 'month','weather']
        labels = {
            "season":"계절",
            "workingday":"주말 또는 주중",
            "month":"월",
            "weather":"날씨",
        }