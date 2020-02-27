from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('form/', views.form , name = 'entry_form'),
    path('list/', views.list),
    path('detail/', views.detail)
]