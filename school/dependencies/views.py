from django.shortcuts import render, redirect, get_object_or_404
from .models import Class, School, Family, Fee_Concession, Section, Session, Religion, Subject, Class_Subject
from .forms import class_form, school_form, family_form, fee_concession_form, section_form, session_form, religion_form, subject_form, classes_subject_form




def class_list(request):
    clas = Class.objects.all()
    context = {'Class': clas}
    return render(request, 'Dependencies/Classes/list.html', context)

def classes(request):
    if request.method == 'POST':
        user_form = class_form(request.POST)
        if user_form.is_valid():
            classes = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Classes/created_classes_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Classes/created_classes_form.html', context)
    else:
        user_form = class_form()
        return render(request,'Dependencies/Classes/classes_form.html',{'user_form':user_form})


def edit_class(request,class_code):
    clas = get_object_or_404(Class, class_code=class_code)
    if request.method == "POST":
        user_form = class_form(request.POST or None, instance=clas)
        if user_form.is_valid():
            user_form.save()
            return redirect('class_list')
    else:
        user_form = class_form(instance=clas)

        return render(request, 'Dependencies/Classes/editclass.html', {'user_form': user_form})

def delete_class(request, class_code):
    Class.objects.filter(class_code=class_code).delete()
    cla = Class.objects.all()

    context = {
        'Class' : cla
    }
    return render(request, 'Dependencies/Classes/list.html', context) 

def school_list(request):
    schol = School.objects.all()
    context = {'school': schol}
    return render(request, 'Dependencies/Schools/list.html', context)


def schools(request):
    if request.method == 'POST':
        user_form = school_form(request.POST)
        if user_form.is_valid():
            schools = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Schools/created_schools_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Schools/created_schools_form.html', context)
    else:
        user_form = school_form()
        return render(request,'Dependencies/Schools/schools_form.html',{'user_form':user_form})


def edit_school(request, school_code):
    schol = get_object_or_404(School, school_code=school_code)

    if request.method == "POST":
        user_form = school_form(request.POST or None, instance=schol)
        if user_form.is_valid():
            user_form.save()
            return redirect('school_list')
    else:
        user_form = school_form(instance=schol)

        return render(request, 'Dependencies/Schools/editschool.html', {'user_form': user_form})


def delete_school(request, school_code):
    School.objects.filter(school_code=school_code).delete()
    sch = School.objects.all()

    context = {
        'school' : sch
    }
    return render(request, 'Dependencies/Schools/list.html', context) 


def family_list(request):
    fami = Family.objects.all()
    context = {'family': fami}
    return render(request, 'Dependencies/Family/list.html', context)


def families(request):
    if request.method == 'POST':
        user_form = family_form(request.POST)
        if user_form.is_valid():
            families = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Family/created_families_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Family/created_families_form.html', context)
    else:
        user_form = family_form()
        return render(request,'Dependencies/Family/families_form.html',{'user_form':user_form})


def edit_family(request, family_code):
    fami = get_object_or_404(Family, family_code=family_code)

    if request.method == "POST":
        user_form = family_form(request.POST or None, instance=fami)
        if user_form.is_valid():
            user_form.save()
            return redirect('family_list')
    else:
        user_form = family_form(instance=fami)

        return render(request, 'Dependencies/Family/editfamily.html', {'user_form': user_form})


def family_detail(request,family_code):
    fmil = get_object_or_404(Family,family_code = family_code)
    context = {
        'family': fmil,
    }
    return render(request, 'Dependencies/Family/detail.html', context)


def delete_family(request, family_code):
    Family.objects.filter(family_code=family_code).delete()
    famil = Family.objects.all()

    context = {
        'family' : famil
    }
    return render(request, 'Dependencies/Family/list.html', context) 


def fee_concession_list(request):
    fee = Fee_Concession.objects.all()
    context = {'fees': fee}
    return render(request, 'Dependencies/FeeConcession/list.html', context)


def fee_concession(request):
    if request.method == 'POST':
        user_form = fee_concession_form(request.POST)
        if user_form.is_valid():
            fee_concession = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/FeeConcession/created_fee_concession_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/FeeConcession/created_fee_concession_form.html', context)
    else:
        user_form = fee_concession_form()
        return render(request,'Dependencies/FeeConcession/fee_concession_form.html',{'user_form':user_form})


def edit_fee_concession(request, fee_concession_code):
    fee = get_object_or_404(Fee_Concession, fee_concession_code=fee_concession_code)

    if request.method == "POST":
        user_form = fee_concession_form(request.POST or None, instance=fee)
        if user_form.is_valid():
            user_form.save()
            return redirect('fee_concession_list')
    else:
        user_form = fee_concession_form(instance=fee)

        return render(request, 'Dependencies/FeeConcession/editfee.html', {'user_form': user_form})


def delete_fee_concession(request, fee_concession_code):
    Fee_Concession.objects.filter(fee_concession_code=fee_concession_code).delete()
    fC = Fee_Concession.objects.all()

    context = {
        'fees' : fC
    }
    return render(request, 'Dependencies/FeeConcession/list.html', context) 


def section_list(request):
    sec = Section.objects.all()
    context = {'section': sec}
    return render(request, 'Dependencies/Sections/list.html', context)


def sections(request):
    if request.method == 'POST':
        user_form = section_form(request.POST)
        if user_form.is_valid():
            sections = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Sections/created_sections_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Sections/created_sections_form.html', context)
    else:
        user_form = section_form()
        return render(request,'Dependencies/Sections/sections_form.html',{'user_form':user_form})


def edit_section(request, sect_code):
    sec = get_object_or_404(Section, sect_code=sect_code)

    if request.method == "POST":
        user_form = section_form(request.POST or None, instance=sec)
        if user_form.is_valid():
            user_form.save()
            return redirect('section_list')
    else:
        user_form = section_form(instance=sec)

        return render(request, 'Dependencies/Sections/editsection.html', {'user_form': user_form})


def delete_section(request, sect_code):
    Section.objects.filter(sect_code=sect_code).delete()
    sect = Section.objects.all()

    context = {
        'section' : sect
    }
    return render(request, 'Dependencies/Sections/list.html', context)
            


def session_list(request):
    sess = Session.objects.all()
    context = {'session': sess}
    return render(request, 'Dependencies/Sessions/list.html', context)


def sessions(request):
    if request.method == 'POST':
        user_form = session_form(request.POST)
        if user_form.is_valid():
            sessions = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Sessions/created_sessions_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Sessions/created_sessions_form.html', context)
    else:
        user_form = session_form()
        return render(request,'Dependencies/Sessions/sessions_form.html',{'user_form':user_form})


def edit_session(request, session_code):
    sess = get_object_or_404(Session, session_code=session_code)

    if request.method == "POST":
        user_form = session_form(request.POST or None, instance=sess)
        if user_form.is_valid():
            user_form.save()
            return redirect('session_list')
    else:
        user_form = session_form(instance=sess)

        return render(request, 'Dependencies/Sessions/editsession.html', {'user_form': user_form})


def delete_session(request, session_code):
    Session.objects.filter(session_code=session_code).delete()
    sessi = Session.objects.all()

    context = {
        'session' : sessi
    }
    return render(request, 'Dependencies/Sessions/list.html', context)

    

def religion_list(request):
    reli = Religion.objects.all()
    context = {'religion': reli}
    return render(request, 'Dependencies/Religions/list.html', context)


def religions(request):
    if request.method == 'POST':
        user_form = religion_form(request.POST)
        if user_form.is_valid():
            religions = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Religions/created_religions_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Religions/created_religions_form.html', context)
    else:
        user_form = religion_form()
        return render(request,'Dependencies/Religions/religions_form.html',{'user_form':user_form})


def edit_religion(request, religion_code):
    reli = get_object_or_404(Religion, religion_code=religion_code)

    if request.method == "POST":
        user_form = religion_form(request.POST or None, instance=reli)
        if user_form.is_valid():
            user_form.save()
            return redirect('religion_list')
    else:
        user_form = religion_form(instance=reli)

        return render(request, 'Dependencies/Religions/editreligion.html', {'user_form': user_form})


def delete_religion(request, religion_code):
    Religion.objects.filter(religion_code=religion_code).delete()
    relig = Religion.objects.all()

    context = {
        'religion' : relig
    }
    return render(request, 'Dependencies/Religions/list.html', context)


def subject_list(request):
    sub = Subject.objects.all()
    context = {'subject': sub}
    return render(request, 'Dependencies/Subjects/list.html', context)


def subjects(request):
    if request.method == 'POST':
        user_form = subject_form(request.POST)
        if user_form.is_valid():
            subjects = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Subjects/created_subjects_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Subjects/created_subjects_form.html', context)
    else:
        user_form = subject_form()
        return render(request,'Dependencies/Subjects/subjects_form.html',{'user_form':user_form})

def edit_subject(request, subject_code):
    sub = get_object_or_404(Class_Subject, subject_code=subject_code)

    if request.method == "POST":
        user_form = subject_form(request.POST or None, instance=sub)
        if user_form.is_valid():
            user_form.save()
            return redirect('subject_list')
    else:
        user_form = subject_form(instance=sub)

        return render(request, 'Dependencies/Subjects/editsubject.html', {'user_form': user_form})



def delete_subject(request, subject_code):

    Subject.objects.filter(subject_code=subject_code).delete()
    subje = Subject.objects.all()

    context = {
        'subject' : subje
    }
    return render(request, 'Dependencies/Subjects/list.html', context)


def class_subject_list(request):
    cla_sub = Class_Subject.objects.all()
    context = {'class_subject': cla_sub}
    return render(request, 'Dependencies/Class_Subjects/list.html', context)

def class_subjects(request):
    if request.method == 'POST':
        user_form = classes_subject_form(request.POST)
        if user_form.is_valid():
            class_subjects = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Class_Subjects/created_class_subject_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Class_Subjects/created_class_subject_form.html', context)
    else:
        user_form = classes_subject_form()
        return render(request,'Dependencies/Class_Subjects/class_subject_form.html',{'user_form':user_form})




def edit_class_subject(request, Class_code):
    cla_sub = get_object_or_404(Class_Subject, Class_code=Class_code)

    if request.method == "POST":
        user_form = classes_subject_form(request.POST or None, instance=cla_sub)
        if user_form.is_valid():
            user_form.save()
            return redirect('class_subject_list')
    else:
        user_form = classes_subject_form(instance=cla_sub)

        return render(request, 'Dependencies/Class_Subjects/editclasssubject.html', {'user_form': user_form})


def class_subject_detail(request,Class_code):
    kla = get_object_or_404(Class_Subject,Class_code = Class_code)
    context = {
        'class_subject': kla,
    }
    return render(request, 'Dependencies/Class_Subjects/detail.html', context)


def delete_class_subject(request, Class_code):
    
    Class_Subject.objects.filter(Class_code=Class_code).delete()
    cla_subj = Class_Subject.objects.all()

    context = {
        'class_subject' : cla_subj
    }
    return render(request, 'Dependencies/Class_Subjects/list.html', context)