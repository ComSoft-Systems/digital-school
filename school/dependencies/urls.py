from django.urls import path
from django.conf.urls import url
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
    path('class_list/',views.class_list, name = 'class_list'),
    path('edit_class/<class_code>+/', views.edit_class, name = 'edit_class'),
    path('delete_class/<class_code>+/', views.delete_class, name = 'delete_class'),
    
    path('school_form/',views.schools, name = 'school_form'),
    path('school_list/',views.school_list, name = 'school_list'),
    path('edit_school/<school_code>+/', views.edit_school, name = 'edit_school'),
    path('delete_school/<school_code>+/', views.delete_school, name = 'delete_school'),

    
    path('family_form/',views.families, name = 'family_form'),
    path('family_list/',views.family_list, name = 'family_list'),
    path('edit_family/<family_code>+/', views.edit_family, name = 'edit_family'),
    path('delete_family/<family_code>+/', views.delete_family, name = 'delete_family'),

    
    path('fee_category_form/',views.fee_categories, name = 'fee_category_form'),
    path('fee_category_list/',views.fee_category_list, name = 'fee_category_list'),
    path('edit_fee_category/<fee_category_code>+/', views.edit_fee_category, name = 'edit_fee_category'),
    path('delete_fee_category/<fee_category_code>+/', views.delete_fee_category, name = 'delete_fee_category'),


    path('section_form/',views.sections, name = 'section_form'),
    path('section_list/',views.section_list, name = 'section_list'),
    path('edit_section/<sect_code>+/', views.edit_section, name = 'edit_section'),
    path('delete_section/<sect_code>+/', views.delete_section, name = 'delete_section'),


    path('session_form/',views.sessions, name = 'session_form'),
    path('session_list/',views.session_list, name = 'session_list'),
    path('edit_session/<session_code>+/', views.edit_session, name = 'edit_session'),
    path('delete_session/<session_code>+/', views.delete_session, name = 'delete_session'),


    path('religion_form/',views.religions, name = 'religion_form'),
    path('religion_list/',views.religion_list, name = 'religion_list'),
    path('edit_religion/<religion_code>+/', views.edit_religion, name = 'edit_religion'),
    path('delete_religion/<religion_code>+/', views.delete_religion, name = 'delete_religion'),


]
