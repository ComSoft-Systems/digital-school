from django.urls import path
from . import views

urlpatterns = [    
    path('', views.ManageMainScreenView, name='MainScreen_url'),
    path('main/', views.ManageAfterLoginView, name='after_login_url'),
    path('about/', views.ManageAboutView, name='about_url'),
    path('school/', views.ManageSchoolView, name='school_url'),
    path('contact/', views.ManageContactView, name='contact_url'),
    path('team/', views.ManageTeamView, name='team_url'),
    path('detail/', views.ManageDetailView, name='detail_url'),
    path('usertype/', views.ManageUserTypeView, name='usertype_url'),
    path('userprofile/', views.ManageUserProfileView, name='userprofile_url'),
    path('usertype/create/', views.ManageUserTypeCreateView, name='usertypecreate_url'),
    path('userprofile/create/', views.ManageUserProfileCreateView, name='userprofilecreate_url'),
]
