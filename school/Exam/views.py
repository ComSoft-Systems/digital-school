import csv, io
from django.shortcuts import render,redirect, get_object_or_404,HttpResponse,get_list_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .filters import Mark_filter, Exam_filter, Semesterbreakup_filter,Semester_filter,Quater_filter,Assesment_filter
from static.renderer import PdfMaker

def hello(request):
    return render(request, 'exam/home_page.html')


def form(request):
    if request.method == 'POST':
        user_form = ExamForm(request.POST)
        if user_form.is_valid():
            form = user_form.save()
            user_form = ExamForm()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'Exam/exam_form.html',{'user_form':user_form})
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


def list_view(request):
    Entry_Exam = Exam.objects.all()
    myFilter = Exam_filter(request.GET, queryset=Entry_Exam)
    Entry_Exam = myFilter.qs
    context = {'Entry': Entry_Exam, 'myFilter':myFilter}
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
            semester_form = SemesterForm()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'semester/semester_form.html',{'semester_form':semester_form})
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'semester/semester_created.html',context)
    else:
        semester_form = SemesterForm()
        return render(request,'semester/semester_form.html',{'semester_form':semester_form})

def semester_list_view(request):
    Entry_Semester = Semester.objects.all()
    myFilter = Semester_filter(request.GET, queryset=Entry_Semester)
    Entry_Semester = myFilter.qs
    context = {'Entry': Entry_Semester,'myFilter':myFilter}
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
            semesterB_form = SemesterbreakupForm()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'semesterB/semesterB_form.html',{'semesterB_form':semesterB_form})
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'semesterB/semesterB_created.html',context)
    else:
        semesterB_form = SemesterbreakupForm()
        return render(request,'semesterB/semesterB_form.html',{'semesterB_form':semesterB_form})


def semesterB_list_view(request):
    Entry_SemesterB = Semesterbreakup.objects.all()
    myFilter = Semesterbreakup_filter(request.GET, queryset=Entry_SemesterB)
    Entry_SemesterB = myFilter.qs
    context = {'Entry': Entry_SemesterB,'myFilter':myFilter}
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
#### QUATER MODEL
def quaterform(request):
    if request.method == 'POST':
        quater_form = QuaterForm(request.POST)
        if quater_form.is_valid():
            form = quater_form.save()
            quater_form = QuaterForm()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'quater/quater_form.html',{'quater_form':quater_form})
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'quater/quater_created.html',context)
    else:
        quater_form = QuaterForm()
        return render(request,'quater/quater_form.html',{'quater_form':quater_form})

def quater_list_view(request):
    Entry_quater = Quater.objects.all()
    myFilter = Quater_filter(request.GET, queryset=Entry_quater)
    Entry_quater = myFilter.qs
    context = {'Entry': Entry_quater,'myFilter':myFilter}
    return render (request,'quater/quater_list.html', context)

def quater_detail(request,quater_code):
    abc = get_object_or_404(Quater,quater_code = quater_code)
    context = {
        'Entry': abc,
    }
    return render(request, 'quater/quater_detail.html', context)

def quater_edit(request,quater_code):
    i = get_object_or_404(Quater, quater_code=quater_code)
    if request.method == "POST":
        quater_form = QuaterForm(request.POST, instance=i)
        if quater_form.is_valid():
            quater_form.save()
            return redirect('quater_list_view')
    else:
        quater_form = QuaterForm(instance=i)
        return render(request, 'quater/edit_quater.html', {'quater_form':quater_form})
    
def quater_delete(request, quater_code):
    Quater.objects.filter(quater_code=quater_code).delete()
    a = Quater.objects.all()
    context = {
        'Entry' : a
    }
    return render(request, 'quater/quater_list.html', context)
####ASSESMENT MODEL
def assesmentform(request):
    if request.method == 'POST':
        assesment_form = AssesmentForm(request.POST)
        if assesment_form.is_valid():
            form = assesment_form.save()
            assesment_form = AssesmentForm()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'assesment/assesment_form.html',{'assesment_form':assesment_form})
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'assesment/assesment_created.html',context)
    else:
        assesment_form = AssesmentForm()
        return render(request,'assesment/assesment_form.html',{'assesment_form':assesment_form})


def assesment_list_view(request):
    Entry_assesment = Assesment.objects.all()
    myFilter = Assesment_filter(request.GET, queryset=Entry_assesment)
    Entry_assesment = myFilter.qs
    context = {'Entry': Entry_assesment,'myFilter':myFilter}
    return render (request,'assesment/assesment_list.html', context)

def assesment_detail(request,assesment_code):
    abc = get_object_or_404(Assesment,assesment_code = assesment_code)
    context = {
        'Entry': abc,
    }
    return render(request, 'assesment/assesment_detail.html', context)

def assesment_edit(request,assesment_code):
    i = get_object_or_404(Assesment, pk=assesment_code)
    print(i)
    if request.method == "POST":
        assesment_form = AssesmentForm(request.POST, instance=i)
        if assesment_form.is_valid():
            assesment_form.save()
            return redirect('assesment_list_view')
    else:
        assesment_form = AssesmentForm(instance=i)
        return render(request, 'assesment/edit_assesment.html', {'assesment_form':assesment_form})
    
def assesment_delete(request, assesment_code):
    Assesment.objects.filter(assesment_code=assesment_code).delete()
    a = Assesment.objects.all()
    context = {
        'Entry' : a
    }
    return render(request, 'assesment/assesment_list.html', context)

####Mark MODEL
def markform(request):
    if request.method == 'POST':
        incoming = request.POST
        clas = incoming.get('class')
        section = incoming.get('section')
        exam = incoming.get('exam')
        for i in exam:
            exam = i
        semester = incoming.get('semester')
        for i in semester:
            semester = i
        semester_b = incoming.get('semester_b')
        for i in semester_b:
            semester_b = i
        quater = incoming.get('quater')
        for i in quater:
            quater = i
        assesment = incoming.get('assesment')
        for i in assesment:
            assesment = i
        subjects = incoming.get('subject')
        for i in subjects:
            subjects = i
        total_marks = incoming.get('total_marks')
        context = {
            'exam' : get_object_or_404(Exam , exam_code = exam) ,
            'semester' : get_object_or_404(Semester , semester_code = semester ) ,
            'semester_b' : get_object_or_404(Semesterbreakup , semesterbreakup_code = semester_b ) ,
            'quater' : get_object_or_404(Quater , quater_code = quater ) ,
            'assesment' : get_object_or_404(Assesment , assesment_code = assesment ) ,
            'subjects' : get_object_or_404(Subject , subject_code = subjects ) ,
            'students' : get_list_or_404(Gr , section = section , current_class = clas ) ,
            'total_marks' : total_marks ,
        }
        return render(request,'mark/mark_entry.html',context)
    else:
        context = {
        'exam' : Exam.objects.all() ,
        'semester' : Semester.objects.all() ,
        'semester_b' : Semesterbreakup.objects.all() ,
        'quater' : Quater.objects.all() ,
        'assesment' : Assesment.objects.all() ,
        'class' : Class.objects.all() ,
        'subjects' : Subject.objects.all() ,
        'section' : Section.objects.all() ,
        }
        return render(request,'mark/mark_form.html',context)

def mark_save(request):
    if request.method == 'POST':
        datatosave = request.POST
        exam = datatosave.get('exam')
        semester = datatosave.get('semester')
        semester_b = datatosave.get('semester_b')
        quater = datatosave.get('quater')
        assesment = datatosave.get('assesment')
        subjects = datatosave.get('subjects')
        gr = datatosave.get('gr')
        obtained_marks = datatosave.get('obtained_marks')
        total_marks = datatosave.get('total')
        count = '0'
        for i in gr:
            count = int(count) + 1
            student = get_object_or_404(Gr , gr_number = gr[int(count)-1])
            grNum = student.gr_number
            class_ = student.current_class
            fname = student.family_code
            formtosave = MarkForm({
                'exam_Gr_no' : (grNum ) ,
                'class_code' : (class_.class_code ) ,
                'subject_code' : (get_object_or_404(Subject , subjects = subjects ).subject_code ) ,
                'exam_code' : (get_object_or_404(Session , session_name = exam).session_code ) ,
                'semester_code' : (get_object_or_404(Semester , semester_name = semester ).semester_code ) ,
                'semesterbreakup_code' : (get_object_or_404(Semesterbreakup , semesterbreakup_name = semester_b ).semesterbreakup_code ) ,
                'quater_code' : (get_object_or_404(Quater , quater_name = quater ).quater_code ) ,
                'assesment_code' : (get_object_or_404(Assesment , assesment_name = assesment ).assesment_code ) ,
                'total_marks' : (total_marks ) ,
                'obtained_marks' : (obtained_marks) ,
             })
            if formtosave.is_valid:
                formtosave.save()
        return render(request,'mark/mark_created.html')

def mark_list_view(request):
    save_mark = Mark.objects.all()
    for i in save_mark:
        nam = i.exam_Gr_no
        gr = get_object_or_404(Gr,name = nam)
        family = gr.family_code
    myFilter = Mark_filter(request.GET, queryset=save_mark)
    save_mark = myFilter.qs
    context = {'father': family, 'save': save_mark ,'myFilter' : myFilter }
    return render (request,'mark/mark_list.html', context)

def mark_detail(request,id):
    abc = get_object_or_404(Mark, id = id)
    context = {
        'Entry': abc,
    }
    return render(request, 'mark/mark_detail.html', context)

def mark_edit(request,id):
    i = get_object_or_404(Mark, id = id)
    if request.method == "POST":
        mark_form = MarkForm(request.POST, instance=i)
        if mark_form.is_valid():
            mark_form.save()
            return redirect('mark_list_view')
    else:
        mark_form = MarkForm(instance=i)
        return render(request, 'mark/edit_mark.html', {'mark_form':mark_form})
    
def mark_delete(request, id):
    Mark.objects.filter(id = id).delete()
    a = Mark.objects.all()
    context = {
        'Entry' : a
    }
    return render(request, 'mark/mark_delete.html', context)

def mark_upload(request):
    template = "mark/mark_upload.html"

    prompt = {
        'order': 'Order by same sequence of mark'
    }
    if request.method == "GET":
        return render(request,"mark/mark_upload.html",prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = MarkForm({
            'exam_Gr_no':column[0], 
            'class_code':column[1],
            'subject_code' :column[2], 
            'exam_code':column[3], 
            'semester_code':column[4], 
            'semesterbreakup_code':column[5],
            'quater_code':column[6], 
            'assesment_code':column[7],
            'total_marks':column[8],
            'obtained_marks':column[9]
        })
        print(created)
        created.save()
    context = {'abc' : 'Added Successfully'}
    return render(request, "mark/mark_upload.html", context)

def markprintsample(request):
    students = []
    data = []
    if request.method == 'POST':
        rawdata = request.POST
        exam_ = rawdata.get('exam')
        semester_ = rawdata.get('semester')
        semester_b_ = rawdata.get('semester_b')
        quater_ = rawdata.get('quater')
        assesment_ = rawdata.get('assesment')
        subjects_ = rawdata.get('subjects')
        total_ = rawdata.get('total')
        stud = rawdata.getlist('stu')
        for i in stud:
            stude = get_object_or_404(Gr , gr_number = i)
            students.append(stude)
        abc = (exam_ ,semester_ ,semester_b_ ,quater_ ,assesment_ ,subjects_ ,total_ )
        data.append(abc)
    context = {
        'data' : data ,
        'student' : students ,
    }
    pdf = PdfMaker("mark/mark_sample_print.html",context)
    return HttpResponse(pdf , content_type='application/pdf')

def markprint(request):
    data = []
    if request.method == 'POST':
        rawdata = request.POST
        id_ = rawdata.getlist('id' , default='1')
        for i in id_:
            mark = get_object_or_404(Mark , pk = i )
            gr__ = mark.exam_Gr_no.name
            class__ = mark.exam_Gr_no.current_class
            section_code_ = mark.section_code
            subject_code_ = mark.subject_code
            exam_code_ = mark.exam_code
            semester_code_ = mark.semester_code
            semesterbreakup_code_ = mark.semesterbreakup_code
            quater_code_ = mark.quater_code
            assesment_code_ = mark.assesment_code
            total_marks_ = mark.total_marks
            obtained_marks_ = mark.obtained_marks
            abc = (gr__ ,class__ ,section_code_ ,subject_code_ ,exam_code_ ,semester_code_ ,semesterbreakup_code_ ,quater_code_ ,assesment_code_ ,total_marks_ ,obtained_marks_ ,)
            data.append(abc)
            print(abc)
    context = {
        'data' : data ,
    }
    pdf = PdfMaker("mark/mark_print.html",context)
    return HttpResponse(pdf , content_type='application/pdf')
    # return render(request , 'mark/mark_print.html',context)

def exam_upload(request):
    template = "exam/exam_upload.html"

    prompt = {
        'order': 'Order by same sequence of exam'
    }
    if request.method == "GET":
        return render(request,"exam/exam_upload.html",prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = ExamForm({ 
            'exam_code':column[0],
            'exam_session':column[1]
        })
        print(created)
        created.save()
    context = {'abc' : 'Added Successfully'}
    return render(request, "exam/exam_upload.html", context)

def semester_upload(request):
    template = "semester/semester_upload.html"

    prompt = {
        'order': 'Order by same sequence of mark'
    }
    if request.method == "GET":
        return render(request,"semester/semester_upload.html",prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = SemesterForm({ 
            'exam_code':column[0],
            'semester_code':column[1],
            'semester_name':column[2],
        })
        print(created)
        created.save()
    context = {'abc' : 'Added Successfully'}
    return render(request, "semester/semester_upload.html", context)

def assesment_upload(request):
    template = "assesment/assesment_upload.html"

    prompt = {
        'order': 'Order by same sequence of assesment'
    }
    if request.method == "GET":
        return render(request,"assesment/assesment_upload.html",prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = AssesmentForm({ 
            'exam_code':column[0],
            'semester_code':column[1],
            'semesterbreakup_code':column[2],
            'quater_code':column[3],
            'assesment_code':column[4],
            'assesment_name':column[5]
        })
        print(created)
        created.save()
    context = {'abc' : 'Added Successfully'}
    return render(request, "assesment/assesment_upload.html", context)

def quater_upload(request):
    template = "quater/quater_upload.html"

    prompt = {
        'order': 'Order by same sequence of assesment'
    }
    if request.method == "GET":
        return render(request,"quater/quater_upload.html",prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = QuaterForm({ 
            'exam_code':column[0],
            'semester_code':column[1],
            'semesterbreakup_code':column[2],
            'quater_code':column[3],
            'quater_name':column[4]
        })
        print(created)
        created.save()
    context = {'abc' : 'Added Successfully'}
    return render(request, "quater/quater_upload.html", context)

def semesterB_upload(request):
    template = "semesterB/semesterB_upload.html"

    prompt = {
        'order': 'Order by same sequence of assesment'
    }
    if request.method == "GET":
        return render(request,"semesterB/semesterB_upload.html",prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = QuaterForm({ 
            'exam_code':column[0],
            'semester_code':column[1],
            'semesterbreakup_code':column[2],
            'semesterbreakup_name':column[3]
        })
        print(created)
        created.save()
    context = {'abc' : 'Added Successfully'}
    return render(request, "semesterB/semesterB_upload.html", context)

def mark_download(request):
    items = Mark.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mark.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['exam_Gr_no','class_code','subject_code','exam_code','semester_code','semesterbreakup_code','quater_code','assesment_code','total_marks','obtained_marks'])
    for obj in items:
        writer.writerow([obj.exam_Gr_no, obj.class_code, obj.subject_code, obj.exam_code, obj.semester_code, obj.semesterbreakup_code, obj.quater_code, obj.assesment_code, obj.total_marks, obj.obtained_marks])
    return response

def exam_download(request):
    items = Exam.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exam.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['exam_code','exam_session'])
    for obj in items:
        writer.writerow([obj.exam_code, obj.exam_session])
    return response

def semester_download(request):
    items = Semester.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="semester.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['exam_code','semester_code','semester_name'])
    for obj in items:
        writer.writerow([obj.exam_code, obj.semester_code, obj.semester_name])
    return response

def semesterbreakup_download(request):
    items = Semesterbreakup.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="semesterbreakup.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['exam_code','semester_code','semesterbreakup_code','semesterbreakup_name'])
    for obj in items:
        writer.writerow([obj.exam_code, obj.semester_code, obj.semesterbreakup_code, obj.semesterbreakup_name])
    return response

def quater_download(request):
    items = Quater.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="quater.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['exam_code','semester_code','semesterbreakup_code','quater_code','quater_name'])
    for obj in items:
        writer.writerow([obj.exam_code, obj.semester_code, obj.semesterbreakup_code, obj.quater_code, obj.quater_name])
    return response

def assesment_download(request):
    items = Assesment.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="assesment.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['exam_code','semester_code','semesterbreakup_code','quater_code','assesment_code','assesment_name'])
    for obj in items:
        writer.writerow([obj.exam_code, obj.semester_code, obj.semesterbreakup_code, obj.quater_code, obj.assesment_code, obj.assesment_name])
    return response