from django.urls import path
from . import views

urlpatterns = [
    path('',views.ManageGrListView, name="gr_list"),
    path('student/create/',views.ManageGrCreateView, name="gr_create"),
    path('<int:gr_number>/',views.ManageGrDetailView,name='gr_detail'),

]
