from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes),
    path('', views.schools),
    path('', views.fee_category),
    path('', views.section),
    path('', views.session),
    path('', views.family),
]
