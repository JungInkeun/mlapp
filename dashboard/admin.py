from django.contrib import admin
from dashboard.models import Data
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['name','age','sex','height','predict']

admin.site.register(Data, DataAdmin)