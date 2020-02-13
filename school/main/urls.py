from django.urls import path
from . import views

urlpatterns = [
    path('digilogin/', views.LoginForm, name='LOGIN'),    
    path('', views.MainScreen, name='MainScreen')
]
