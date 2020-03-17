from django.shortcuts import render
from .models import *
from student_information.models import *
from dependencies.models import *
from .forms import *


# def attendance_add(CreateView):
#     list_of_student = SaveAttendence.objects.all()

#     if CreateView.method == 'POST':
#         user_form = Attendence_Form(CreateView.POST)
#         if user_form.is_valid():
#             form = user_form.save()
#             context = {
#                 'return': 'Has Been Added SuccessFully'
#             }
#             return render(CreateView,'added.html',context)
#         else:
#             context = {
#                 'return': 'Is Not Valid'
#             } 
#             return render(CreateView,'added.html',context)
#     else:
#         user_form = Attendence_Form()
#         log = {'form':user_form, 'Show': list_of_student}
#         return render(CreateView, 'attendence_for_all.html', log)



def attendance_add(CreateView):
    if CreateView.method == "POST":
        blank_list = []
        clas = CreateView.POST.get('clas')
        gr_fields = Gr.objects.all()
        for gr_rows in gr_fields:
            if str(gr_rows.current_class) == str(clas):
                blank_list.append(str(gr_rows.gr_number,gr_rows.name))
                # gr = (grows.gr_number)
                # name = (grows.name)
                # family = (grows.family_code)
                # clas = (grows.current_class)
        log = {'blank_list': blank_list, 'gr_fields': gr_fields}
        return render(CreateView, 'cde.html', log)
    else:
        clas = Gr.objects.all()
        log = {'attend' : clas}
        return render(CreateView, 'attendence_for_all.html', log)

