from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes),
    path('schools/', views.schools),
    path('fee_category/', views.fee_category),
    path('sections/', views.section),
    path('sessions/', views.session),
    path('family', views.family),
]
