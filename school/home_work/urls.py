from django.urls import path
from . import views

urlpatterns = [
    # path('home_work/', views.home_work, name="home_work_main"),
    # path('home_work/calender/', views.home_work_calender, name="home_work_calender"),
    path('homework/create/', views.home_work_info, name='home_work_create'),

]
