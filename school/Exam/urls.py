from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('hello/', views.hello),
    ### exam model....
    path('form/', views.form , name = 'exam_form'),
    path('list_view/', views.list_view, name = 'exam_list_view'),
    path('edit/<exam_code>+/', views.edit, name='edit_exam'),
    path('delete/<exam_code>+/', views.delete, name='delete_exam'),
    path('detail/<exam_code>/', views.detail, name = 'exam_detail'),
    ### SEMESTER MODEL
    path('semester_form/', views.semester_form , name = 'semester_form'),
    path('semester_list_view/', views.semester_list_view, name = 'semester_list_view'),
    path('semester_edit/<semester_code>+/', views.semester_edit, name='edit_semester'),
    path('semester_delete/<semester_code>+/', views.semester_delete, name='delete_semester'),
    path('semester_detail/<semester_code>/', views.semester_detail, name = 'semester_detail'),
    ### SEMESTER Breakup MODEL
    path('semesterB_form/', views.semesterBform , name = 'semesterB_form'),
    path('semesterB_list_view/', views.semesterB_list_view, name = 'semesterB_list_view'),
    path('semesterB_detail/<semesterbreakup_code>/', views.semesterB_detail, name = 'semesterB_detail'),
    path('semesterB_edit/<semesterbreakup_code>+/', views.semesterB_edit, name='edit_semesterB'),
    path('semesterB_delete/<semesterbreakup_code>+/', views.semesterB_delete, name='delete_semesterB')
]
    