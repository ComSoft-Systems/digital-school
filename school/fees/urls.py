from django.urls import path
from . import views

urlpatterns = [
    path('type/',views.ManageFeeTypeListView, name="fee_type_list"),
    path('type/create/',views.ManageFeeTypeCreateView, name="fee_type_create"),
    path('type/edit/<fee_type_code>/', views.ManageFeeTypeEditView, name = 'fee_type_edit'),
    path('type/delete/<fee_type_code>/', views.ManageFeeTypeDeleteView, name = 'fee_type_delete'),

    path('def/',views.ManageFeeDefListView, name="fee_def_list"),
    path('def/create/',views.ManageFeeDefCreateView, name="fee_def_create"),
    path('def/edit/<fee_def_code>/', views.ManageFeeDefEditView, name = 'fee_def_edit'),
    path('def/delete/<fee_def_code>/', views.ManageFeeDefDeleteView, name = 'fee_def_delete'),

    path('reg/',views.ManageFeeRegisterListView, name="fee_reg_list"),
    path('reg/create/',views.ManageFeeRegisterCreateView, name="fee_reg_create"),
    path('reg/detail/<fee_reg_id>/',views.ManageFeeRegisterDetailView, name="fee_reg_detail"),
    path('reg/edit/<fee_reg_id>/', views.ManageFeeRegisterEditView, name = 'fee_reg_edit'),
    path('reg/delete/<fee_reg_id>/', views.ManageFeeRegisterDeleteView, name = 'fee_reg_delete'),
]
