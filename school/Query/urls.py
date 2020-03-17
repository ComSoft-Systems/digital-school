from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('home/', views.home),
    path('form/', views.form , name = 'entry_form'),
    path('list_view/', views.list_view, name = 'list_view'),
    path('edit/<Query_code>+/', views.edit, name='edit_query'),
    path('delete/<Query_code>+/', views.delete, name='delete_query'),
    path('detail/<Query_code>/', views.detail, name = 'entry_detail'),
    path('query_upload/', views.query_upload , name = 'query_upload')
]