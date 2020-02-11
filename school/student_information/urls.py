from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.ManageGrListView, name="gr_list"),
    # path('student/<name>',views.ManageGrDetailView,name='gr_detail'),
    path('family/',views.ManageFamilyListView,name='family_list'),
    # path('family/<name>',views.ManageFamilyDetailView,name='family_detail'),

]
