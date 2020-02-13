from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginForm, name='LOGIN'),
    path('digischool/', views.MainScreen, name='MainScreen')
]
