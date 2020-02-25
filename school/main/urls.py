from django.urls import path
from . import views

urlpatterns = [    
    path('', views.MainScreen, name='MainScreen'),
    path('digilogin/', views.LoginForm, name='LOGIN'),
    path('about/', views.about, name='about'),
    path('school/', views.school, name='school'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('detail/', views.detail, name='detail'),
    path('digilogin/main', views.afterlogin, name='after_login')
]
