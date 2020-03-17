from django.urls import path
from . import views

urlpatterns = [
    path('',views.ManageGrListView, name="gr_list"),
    path('create/',views.ManageGrCreateView, name="gr_create"),
    path('create/bulk/', views.ManageGrUploadView, name = 'gr_bulk'),
    path('<int:gr_number>/',views.ManageGrDetailView,name='gr_detail'),
    path('edit/<gr_number>/', views.ManageGrEditView, name = 'gr_edit'),
    path('delete/<gr_number>/', views.ManageGrDeleteView, name = 'gr_delete'),
]
