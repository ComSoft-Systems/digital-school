from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
 
   
    path('class_form/',views.classes, name = 'class_form'),
    path('class_list/',views.class_list, name = 'class_list'),
    # path('class_save/',views.save_classes, name = 'class_save'),
    path('edit_class/<class_code>+/', views.edit_class, name = 'edit_class'),
    path('delete_class/<class_code>+/', views.delete_class, name = 'delete_class'),
    
    path('school_form/',views.schools, name = 'school_form'),
    path('school_list/',views.school_list, name = 'school_list'),
    path('edit_school/<school_code>+/', views.edit_school, name = 'edit_school'),
    path('delete_school/<school_code>+/', views.delete_school, name = 'delete_school'),

    
    path('family_form/',views.families, name = 'family_form'),
    path('family_list/',views.family_list, name = 'family_list'),
    path('edit_family/<family_code>+/', views.edit_family, name = 'edit_family'),
    path('family_detail/<family_code>/', views.family_detail, name = 'family_detail'),
    path('delete_family/<family_code>+/', views.delete_family, name = 'delete_family'),

    
    path('fee_concession_form/',views.fee_concession, name = 'fee_concession_form'),
    path('fee_concession_list/',views.fee_concession_list, name = 'fee_concession_list'),
    path('edit_concession/<fee_concession_code>+/', views.edit_fee_concession, name = 'edit_fee_concession'),
    path('delete_fee_concession/<fee_concession_code>+/', views.delete_fee_concession, name = 'delete_fee_concession'),


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


    path('subject_form/',views.subjects, name = 'subject_form'),
    path('subject_list/',views.subject_list, name = 'subject_list'),
    path('edit_subject/<subject_code>+/',views.edit_subject, name = 'edit_subject'),
    path('delete_subject/<subject_code>+/', views.delete_subject, name = 'delete_subject'),

    path('class_subject_form/',views.class_subjects, name = 'class_subject_form'),
    path('class_subject_list/',views.class_subject_list, name = 'class_subject_list'),
    path('edit_class_subject/<Class_code>+/',views.edit_class_subject, name = 'edit_class_subject'),
    path('class_subject_detail/<Class_code>/', views.class_subject_detail, name = 'class_subject_detail'),
    path('delete_class_subject/<Class_code>+/', views.delete_class_subject, name = 'delete_class_subject'),

    path('fee_type_form/',views.fee_type, name = 'fee_type_form'),
    path('fee_type_list/',views.fee_type_list, name = 'fee_type_list'),
    path('edit_fee_type/<fee_type_code>+/', views.edit_fee_type, name = 'edit_fee_type'),
    path('delete_fee_type/<fee_type_code>+/', views.delete_fee_type, name = 'delete_fee_type'),

    path('month_list/',views.month_list, name = 'month_list'),
    path('month_form/',views.months, name = 'month_form'),


    path('city_list/',views.city_list, name = 'city_list'),
    path('city_form/',views.cities, name = 'city_form'),

]
