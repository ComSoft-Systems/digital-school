from django.shortcuts import render
from .models import *
from student_information.models import *
from dependencies.models import *
# from .filters import studentFilter


def CLA():
    Cla = Class.objects.all()
    return Cla


def SEC():
    Sec = Section.objects.all()
    return Sec


def GR():
    gr = Gr.objects.all()
    return gr


def Filter(InClasses,InSection):
    pass
    

def attendance_save(CreateView):
    if CreateView.method == "POST":
        pass
    return render(CreateView, 'attendence_for_all.html')


def attendance_add(CreateView):
    if CreateView.method == 'POST':
        InClasses = CreateView.POST.get('class')
        InSection = CreateView.POST.get('section')
        InDate = CreateView.POST.get('date')
        stu = []
        for i in GR():
            if str(i.current_class) == str(InClasses):
                stu.append(i)
                classes = CLA()
                section = SEC()
                context = {
                    'attend' : stu,
                    'class' : classes,
                    'section' : section,
                    'date' : InDate,
                }
        return render(CreateView, 'attendence_for_all.html',context)
    else:
        classes = CLA()
        section = SEC()
        clas = GR()
        log = {
            'attend' : clas,
            'class' : classes,
            'section' : section,
            }
        return render(CreateView, 'attendence_for_all.html', log)