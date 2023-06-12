from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('', views.index, name="dashboard-index"),
    path('prediction/', views.prediction, name="dashboard-prediction"),
]
