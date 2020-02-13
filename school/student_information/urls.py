from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.ManageGrListView, name="gr_list"),
    path('student/create/',views.ManageGrCreateView, name="gr_create"),
    path('student/<name>/',views.ManageGrDetailView,name='gr_detail'),

]
