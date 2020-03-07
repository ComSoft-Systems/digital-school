from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import ExamForm, SemesterForm, SemesterbreakupForm
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only

def hello(request):
    return render(request, 'exam/home_page.html')

##### EXAM MODEL ....
def form(request):
    if request.method == 'POST':
        user_form = ExamForm(request.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'Exam/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'Exam/created.html',context)
    else:
        user_form = ExamForm()
        return render(request,'exam/exam_form.html',{'user_form':user_form})


def detail(request,exam_code):
    abc = get_object_or_404(Exam,exam_code = exam_code)
    context = {
        'Entry': abc,
    }
    return render(request, 'exam/exam_detail.html', context)

@login_required(login_url='login_url')
def list_view(request):
    Entry_Exam = Exam.objects.all()
    context = {'Entry': Entry_Exam}
    return render (request,'exam/exam_list.html', context)

def edit(request,exam_code):
    i = get_object_or_404(Exam, exam_code=exam_code)
    if request.method == "POST":
        user_form = ExamForm(request.POST, instance=i)
        if user_form.is_valid():
            user_form.save()
            return redirect('exam_list_view')
    else:
        user_form = ExamForm(instance=i)
        return render(request, 'exam/edit_exam.html', {'user_form':user_form})
    
def delete(request, exam_code):
    Exam.objects.filter(exam_code=exam_code).delete()
    a = Exam.objects.all()

    context = {
        'Entry' : a
    }
    return render(request, 'exam/exam_list.html', context)

#### Semester model
def semester_form(request):
    if request.method == 'POST':
        semester_form = SemesterForm(request.POST)
        if semester_form.is_valid():
            form = semester_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'exam/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'exam/created.html',context)
    else:
        semester_form = SemesterForm()
        return render(request,'semester/semester_form.html',{'semester_form':semester_form})

def semester_list_view(request):
    Entry_Semester = Semester.objects.all()
    context = {'Entry': Entry_Semester}
    return render (request,'semester/semester_list.html', context)

def semester_edit(request,semester_code):
    i = get_object_or_404(Semester, semester_code=semester_code)
    if request.method == "POST":
        semester_form = SemesterForm(request.POST, instance=i)
        if semester_form.is_valid():
            semester_form.save()
            return redirect('semester_list_view')
    else:
        semester_form = SemesterForm(instance=i)
        return render(request, 'semester/edit_semester.html', {'semester_form':semester_form})
    
def semester_delete(request, semester_code):
    Semester.objects.filter(semester_code=semester_code).delete()
    a = Semester.objects.all()
    context = {
        'Entry' : a
    }
    return render(request, 'semester/semester_list.html', context)

def semester_detail(request,semester_code):
    abc = get_object_or_404(Semester,semester_code = semester_code)
    context = {
        'Entry': abc,
    }
    return render(request, 'semester/semester_detail.html', context)
#####SEMESTERBREAKUP MODEL
def semesterBform(request):
    if request.method == 'POST':
        semesterB_form = SemesterbreakupForm(request.POST)
        if semesterB_form.is_valid():
            form = semesterB_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'Exam/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'Exam/created.html',context)
    else:
        semesterB_form = SemesterbreakupForm()
        return render(request,'semesterB/semesterB_form.html',{'semesterB_form':semesterB_form})


def semesterB_list_view(request):
    Entry_SemesterB = Semesterbreakup.objects.all()
    context = {'Entry': Entry_SemesterB}
    return render (request,'semesterB/semesterB_list.html', context)

def semesterB_detail(request,semesterbreakup_code):
    abc = get_object_or_404(Semesterbreakup,semesterbreakup_code = semesterbreakup_code)
    context = {
        'Entry': abc,
    }
    return render(request, 'semesterB/semesterB_detail.html', context)

def semesterB_edit(request,semesterbreakup_code):
    i = get_object_or_404(Semesterbreakup, semesterbreakup_code=semesterbreakup_code)
    if request.method == "POST":
        semesterB_form = SemesterbreakupForm(request.POST, instance=i)
        if semesterB_form.is_valid():
            semesterB_form.save()
            return redirect('semesterB_list_view')
    else:
        semesterB_form = SemesterbreakupForm(instance=i)
        return render(request, 'semesterB/edit_semesterB.html', {'semesterB_form':semesterB_form})
    
def semesterB_delete(request, semesterbreakup_code):
    Semesterbreakup.objects.filter(semesterbreakup_code=semesterbreakup_code).delete()
    a = Semesterbreakup.objects.all()
    context = {
        'Entry' : a
    }
    return render(request, 'semesterB/semesterB_list.html', context)