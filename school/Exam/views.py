from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import ExamForm
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only

def hello(request):
    return render(request, 'exam/home_page.html')


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
        return render(request,'Exam/exam_form.html',{'user_form':user_form})

