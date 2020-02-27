from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('form/', views.form , name = 'entry_form'),
    path('list_view/', views.list_view, name = 'list_view'),
    path('edit/', views.edit, name = 'edit_query'),
    path('detail/<Query_code>/', views.detail, name = 'entry_detail'),
]