from django.contrib import admin
from regression.models import BikeData
# Register your models here.

class BikeDataAdmin(admin.ModelAdmin):
    list_display = ['season', 'workingday', 'month', 
                    'weather', 'date', 'predict_count']
    
admin.site.register(BikeData, BikeDataAdmin)

