from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('book_list/',views.book_list, name = 'book_list'),
    path('book_form/',views.books, name = 'book_form'),
    path('edit_book/<book_code>+/', views.edit_book, name = 'edit_book'),
        path('book_detail/<book_code>/', views.book_detail, name = 'book_detail'),
    path('delete_book/<book_code>+/', views.delete_book, name = 'delete_book'),


    path('publisher_list/',views.publisher_list, name = 'publisher_list'),
    path('publisher_form/',views.publishers, name = 'publisher_form'),
    path('edit_publisher/<publisher_code>+/', views.edit_publisher, name = 'edit_publisher'),
    path('delete_publisher/<publisher_code>+/', views.delete_publisher, name = 'delete_publisher'),


    path('chapter_list/',views.chapter_list, name = 'chapter_list'),
    path('chapter_form/',views.chapters, name = 'chapter_form'),
    path('edit_chapter/<chapter_code>+/', views.edit_chapter, name = 'edit_chapter'),
    path('delete_chapter/<chapter_code>+/', views.delete_chapter, name = 'delete_chapter'),


    path('question_type_list/',views.question_type_list, name = 'question_type_list'),
    path('question_type_form/',views.questions_types, name = 'question_type_form'),
    path('edit_question_type/<Q_type_code>+/', views.edit_question_type, name = 'edit_question_type'),
    path('delete_question_type/<Q_type_code>+/', views.delete_question_type, name = 'delete_question_type'),


    path('question_bank_list/',views.question_bank_list, name = 'question_bank_list'),
    path('question_bank_form/',views.question_banks, name = 'question_bank_form'),
    path('edit_question_bank/<question_code>+/', views.edit_question_bank, name = 'edit_question_bank'),
    path('question_bank_detail/<question_code>/', views.question_bank_detail, name = 'question_bank_detail'),
    path('delete_question_bank/<question_code>+/', views.delete_question_bank, name = 'delete_question_bank'),

]