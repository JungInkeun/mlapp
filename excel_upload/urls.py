from django.urls import path
from excel_upload import views

app_name = "excel_upload"

urlpatterns = [
    path('', views.upload_page, name="upload_page"),
]
