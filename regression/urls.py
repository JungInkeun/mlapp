from django.urls import path
from regression import views

app_name = "regression"

urlpatterns = [
    path('', views.reg_index, name="reg-index")
]
