from django.urls import path
from . import views

urlpatterns = [    
    path('', views.MainScreen, name='MainScreen'),
    path('digilogin/', views.LoginForm, name='LOGIN')
]
