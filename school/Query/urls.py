from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.home),
    path('form/', views.form),
    path('list/', views.list),
    path('detail/', views.detail),
    path('e_list/', views.Entry_data_list, name='Entry_data_list'),
    path('e_detail/', views.Entry_data_detail, name='Entry_data_detail')
]