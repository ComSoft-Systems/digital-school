from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Publisher, Chapter, Question_Type, Question_Bank
from .forms import book_form, publisher_form, chapter_form, question_type_form, question_bank_form
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .filters import Question_Bank_filter
import random 
from dependencies.models import *
# from dependencies.forms import *

# Create your views here.
@login_required(login_url='login_url')
def book_list(request):
    boo = Book.objects.all()
    context = {'book': boo}
    return render(request, 'Question_Bank/Books/list.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def books(request):
    if request.method == 'POST':
        user_form = book_form(request.POST)
        if user_form.is_valid():
            books = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Books/created_book_form.html', context)
            
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Books/created_book_form.html', context)
    else:
        user_form = book_form()
        return render(request,'Question_Bank/Books/book_form.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def edit_book(request,book_code):
    boo = get_object_or_404(Book, book_code=book_code)
    if request.method == "POST":
        user_form = book_form(request.POST or None, instance=boo)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Books/created_book_form.html', context)
    else:
        user_form = book_form(instance=boo)

        return render(request, 'Question_Bank/Books/editbook.html', {'user_form': user_form})

def book_detail(request,book_code):
    bk = get_object_or_404(Book,book_code = book_code)
    context = {
        'book': bk,
    }
    return render(request, 'Question_Bank/Books/detail.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def delete_book(request, book_code):
    Book.objects.filter(book_code=book_code).delete()
    bo = Book.objects.all()

    context = {
        'book' : bo
    }
    return render(request, 'Question_Bank/Books/list.html', context) 

@login_required(login_url='login_url')
def publisher_list(request):
    pub = Publisher.objects.all()
    context = {'publisher': pub}
    return render(request, 'Question_Bank/Publishers/list.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def publishers(request):
    if request.method == 'POST':
        user_form = publisher_form(request.POST)
        if user_form.is_valid():
            publishers = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Publishers/created_publisher_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Publishers/created_publisher_form.html', context)
    else:
        user_form = publisher_form()
        return render(request,'Question_Bank/Publishers/publisher_form.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def edit_publisher(request,publisher_code):
    pub = get_object_or_404(Book, publisher_code=publisher_code)
    if request.method == "POST":
        user_form = publisher_form(request.POST or None, instance=pub)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Publishers/created_publisher_form.html', context)
    else:
        user_form = publisher_form(instance=pub)

        return render(request, 'Question_Bank/Publishers/editpublisher.html', {'user_form': user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def delete_publisher(request, publisher_code):
    Publisher.objects.filter(publisher_code=publisher_code).delete()
    publi = Publisher.objects.all()

    context = {
        'publisher' : publi
    }
    return render(request, 'Question_Bank/Publishers/list.html', context) 

@login_required(login_url='login_url')
def chapter_list(request):
    chap = Chapter.objects.all()
    context = {'chapter': chap}
    return render(request, 'Question_Bank/Chapters/list.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def chapters(request):
    if request.method == 'POST':
        user_form = chapter_form(request.POST)
        if user_form.is_valid():
            chapters = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Chapters/created_chapter_form.html', context)
            
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Chapters/created_chapter_form.html', context)
    else:
        user_form = chapter_form()
        return render(request,'Question_Bank/Chapters/chapter_form.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def edit_chapter(request,chapter_code):
    chap = get_object_or_404(Chapter, chapter_code=chapter_code)
    if request.method == "POST":
        user_form = chapter_form(request.POST or None, instance=chap)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Chapters/created_chapter_form.html', context)
    else:
        user_form = chapter_form(instance=chap)

        return render(request, 'Question_Bank/Chapters/editchapter.html', {'user_form': user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def delete_chapter(request, chapter_code):
    Chapter.objects.filter(chapter_code=chapter_code).delete()
    chapt = Chapter.objects.all()

    context = {
        'chapter' : chapt
    }
    return render(request, 'Question_Bank/Chapters/list.html', context)

@login_required(login_url='login_url')
def question_type_list(request):
    QT = Question_Type.objects.all()
    context = {'question_type': QT}
    return render(request, 'Question_Bank/Question_Type/list.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def questions_types(request):
    if request.method == 'POST':
        user_form = question_type_form(request.POST)
        if user_form.is_valid():
            question_types = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Type/created_question_type_form.html', context)
            
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Question_Type/created_question_type_form.html', context)
    else:
        user_form = question_type_form()
        return render(request,'Question_Bank/Question_Type/question_type_form.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def edit_question_type(request,Q_type_code):
    QT = get_object_or_404(Question_Type, Q_type_code=Q_type_code)
    if request.method == "POST":
        user_form = question_type_form(request.POST or None, instance=QT)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Type/created_question_type_form.html', context)
    else:
        user_form = question_type_form(instance=QT)

        return render(request, 'Question_Bank/Question_Type/editquestiontype.html', {'user_form': user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def delete_question_type(request, Q_type_code):
    Question_Type.objects.filter(Q_type_code=Q_type_code).delete()
    quesT = Question_Type.objects.all()

    context = {
        'question_type' : quesT
    }
    return render(request, 'Question_Bank/Question_Type/list.html', context)

# @login_required(login_url='login_url')
def question_bank_list(request):
    quest = Question_Bank.objects.all()
    myFilter = question_bank_form()
    context = {'question_bank': quest , 'myFilter' : myFilter}
    return render(request, 'Question_Bank/Question_Bank/list.html', context)

def filtered_Questions(request):
    if request.method == 'POST':
        InSubject = request.POST.get('subject')
        InClass = request.POST.get('classes')
        InBook = request.POST.get('book')
        InChapter = request.POST.get('chapter')
        InQuestionType = request.POST.get('question_type')
        # InQuestionFrom = request.POST.get('questions_from')
        InQuantity = request.POST.get('qty')
        pool= list(Question_Bank.objects.all())
        # print(Class)
        context = {'question_bank': 'No Matching Questions Found'}
        Ques = []
        for prows in pool:
            p_rows = prows
            for srows in Subject.objects.all():
                s_rows = srows
                for crows in Class.objects.all():
                    c_rows = crows
                    for brows in Book.objects.all():
                        b_rows = brows
                        for chrows in Chapter.objects.all():
                            ch_rows = chrows
                            for qtrows in Question_Type.objects.all():
                                qt_rows = qtrows
                                # for qfrows in Question_Bank.objects.all():
                                #     qf_rows = qfrows
                                if str(s_rows.subject_code) == str(InSubject):
                                    if str(s_rows.subjects) == str(p_rows.subject):
                                        if str(c_rows.class_code) == str(InClass):
                                            if str(c_rows.class_name) == str(p_rows.classes):
                                                if str(b_rows.book_code) == str(InBook):
                                                    if str(b_rows.book_name) == str(p_rows.book):
                                                        if str(ch_rows.chapter_code) == str(InChapter):
                                                            if str(ch_rows.chapter_name) == str(p_rows.chapter):
                                                                if str(qt_rows.Q_type_code) == str(InQuestionType):
                                                                    if str(qt_rows.question_type) == str(p_rows.question_type):
                                                                        # if str(qf_rows.question_code) == str(InQuestionFrom):
                                                                        #     if str(qf_rows.questions_from) == str(p_rows.questions_from):
                                                        
                                                                        Ques.append(p_rows.question)
                                                                        random.shuffle( Ques )
                                                                        object_list = Ques[:int(InQuantity)]
                                                                        context = {'question_bank': object_list}
        return render(request, 'Question_Bank/Question_Bank/filter.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def question_banks(request):
    if request.method == 'POST':
        user_form = question_bank_form(request.POST)
        if user_form.is_valid():
            question_banks = user_form.save()

            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Bank/created_question_bank_form.html', context)

        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Question_Bank/created_question_bank_form.html', context)
    else:
        user_form = question_bank_form()
        return render(request,'Question_Bank/Question_Bank/question_bank_form.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def edit_question_bank(request,question_code):
    quest = get_object_or_404(Question_Bank, question_code=question_code)
    if request.method == "POST":
        user_form = question_bank_form(request.POST or None, instance=quest)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Bank/created_question_bank_form.html', context)
    else:
        user_form = question_bank_form(instance=quest)

        return render(request, 'Question_Bank/Question_Bank/editquestionbank.html', {'user_form': user_form})


def question_bank_detail(request,question_code):
    queb = get_object_or_404(Question_Bank,question_code = question_code)
    context = {
        'question_bank': queb,
    }
    return render(request, 'Question_Bank/Question_Bank/detail.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def delete_question_bank(request, question_code):
    Question_Bank.objects.filter(question_code=question_code).delete()
    QB = Question_Bank.objects.all()

    context = {
        'question_bank' : QB
    }
    return render(request, 'Question_Bank/Question_Bank/list.html', context) 

# def create_random(request):
#     if request.method == 'POST':
#         in_c = request.POST.get('classes')
#         in_s = request.POST.get('subject')
#         in_b = request.POST.get('book')
#         in_ch = request.POST.get('chapter')
#         in_qt = request.POST.get('question_type')
#         in_qf = request.POST.get('questions_from')
#         in_q = request.POST.get('quantity')
#         print(in_c)
#         print(in_s)
#         print(in_b)
#         print(in_ch)
#         print(in_qt)
#         print(in_qf)
#         print(in_q)
#         question = Question_Bank.objects.all()
#         for qrows in question:
#             q_rows = qrows
#             if str(q_rows.classes) == str(in_c):
#                 if str(q_rows.subject) == str(in_s):
#                     if str(q_rows.book) == str(in_b):
#                         if str(q_rows.chapter) == str(in_ch):
#                             if str(q_rows.question_type) == str(in_qt):
#                                 if str(q_rows.questions_from) == str(in_qf):
#                                     print('abc')
#         return render(request,'Question_Bank/Question_Bank/list.html')
#     else:
#         classes = class_form()
#         subject = subject_form()
#         book = book_form()
#         chapter = chapter_form()
#         questiontype = question_type_form()
#         context = {
#             'classes' : classes ,
#             'subject' : subject ,
#             'book' : book ,
#             'chapter' : chapter ,
#             'questiontype' : questiontype ,
#             }
#         return render(request,'Question_Bank/Question_Bank/random.html',context)








# def ManageRandomView(RandomView):
#     if RandomView.method == 'POST':
#         Clas = RandomView.POST.get('clas')
#         subject = RandomView.POST.get('subject')
#         book = RandomView.POST.get('book')
#         chapter = RandomView.POST.get('chapter')
#         question_type = RandomView.POST.get('question_type')
#         context = {
#             'clas' : Clas,
#             'subject' : subject,
#             'book' : book,
#             'chapter' : chapter,
#             'question_type' : question_type,
#         }
#         pass

#     else:
#         klas = Class.objects.all()
#         sub = Subject.objects.all()
#         boo = Book.objects.all()
#         chap = Chapter.objects.all()
#         qut = Question_Type.objects.all()
#         context = {
#             'klas' : klas,
#             'sub' : sub,
#             'boo' : boo,
#             'chap' : chap,
#             'qut' : qut
#         }
#         return render(RandomView , 'Question_Bank/Question_Bank/random.html' , context)
