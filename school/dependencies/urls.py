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
    path('sessions/', views.ManageSessionsListView),
    path('sessions/<name>/', views.ManageSessionsDetailView),
    path('family/', views.ManageFamilyListView),
    path('family/<name>/', views.ManageFamilyDetailView),
    path('religion/',views.ManageReligionsListView),
    path('religion/<name>/',views.ManageReligionsDetailView),
   
    path('class_form/',views.classes, name = 'class_form'),
    path('school_form/',views.schools, name = 'school_form'),
    path('family_form/',views.families, name = 'family_form'),
    path('fee_category_form/',views.fee_categories, name = 'fee_category_form'),
    path('section_form/',views.sections, name = 'section_form'),
    path('session_form/',views.sessions, name = 'session_form'),
    path('religion_form/',views.religions, name = 'religion_form')

]
