from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('form/', views.form , name = 'exam_form'),
]