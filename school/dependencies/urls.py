from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.ManageClassesListView),
    path('classes/<name>/', views.ManageClassesDetailView),
    path('schools/', views.ManageSchoolsListView),
    path('schools/<name>/', views.ManageSchoolsDetailView),
    path('fee_category/', views.ManageFeeCategoryListView),
    path('fee_category/<name>/', views.ManageFeeCategoryDetailView),
    path('sections/', views.ManageSectionsListView),
    path('sections/<name>/', views.ManageSectionsDetailView),
    path('sessions/', views.session),
    path('family', views.ManageFamilyListView),
    path('family/<name>/', views.ManageFamilyDetailView),
]
