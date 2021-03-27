from django.urls import path
from . import views

urlpatterns = [
    path('i/', views.index, name="index"),
    path('w/', views.welcome, name="welcome")
]