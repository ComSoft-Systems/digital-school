from django.shortcuts import render, redirect, get_object_or_404
from .models import Class, School, Family, Fee_Category, Section, Session, Religion
from .forms import class_form, school_form, family_form, fee_category_form, section_form, session_form, religion_form


def ManageClassesListView(ListView):
    model = Class()
    return render (ListView,'Dependencies/Classes/list.html')

def ManageClassesDetailView(DetailView):
    model = Class()
    return render (DetailView,'Dependencies/Classes/list.html')


def ManageSchoolsListView(ListView):
    model = School()
    return render (ListView,'Dependencies/Schools/list.html')

def ManageSchoolsDetailView(DetailView):
    model = School()
    return render (DetailView,'Dependencies/Schools/list.html')

def ManageFeeCategoryListView(ListView):
    model = Fee_Category()
    return render (ListView,'Dependencies/FeesCategory/list.html')

def ManageFeeCategoryDetailView(DetailView):
    model = Fee_Category()
    return render (DetailView,'Dependencies/FeesCategory/list.html')

def ManageSectionsListView(ListView):
    model = Section()
    return render(ListView, 'Dependencies/Sections/list.html')

def ManageSectionsDetailView(DetailView):
    model = Section()
    return render(DetailView, 'Dependencies/Sections/list.html')

def ManageFamilyListView(ListView):
    model = Family()
    return render (ListView,'Dependencies/Family/list.html')

def ManageFamilyDetailView(DetailView):
    model = Family()
    return render (DetailView,'Dependencies/Family/list.html')

def ManageSessionsListView(ListView):
    model = Session()
    return render(ListView, 'Dependencies/Sessions/list.html')

def ManageSessionsDetailView(DetailView):
    model = Session()
    return render(DetailView, 'Dependencies/Sessions/list.html')

def ManageReligionsListView(ListView):
    model = Religion()
    return render(ListView, 'Dependencies/Religions/list.html')

def ManageReligionsDetailView(DetailView):
    model = Religion()
    return render(DetailView, 'Dependencies/Religions/list.html')



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


def delete_family(request, family_code):
    Family.objects.filter(family_code=family_code).delete()
    famil = Family.objects.all()

    context = {
        'family' : famil
    }
    return render(request, 'Dependencies/Family/list.html', context) 


def fee_category_list(request):
    fee = Fee_Category.objects.all()
    context = {'fees': fee}
    return render(request, 'Dependencies/FeeCategory/list.html', context)


def fee_categories(request):
    if request.method == 'POST':
        user_form = fee_category_form(request.POST)
        if user_form.is_valid():
            fee_categories = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/FeeCategory/created_fee_categories_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/FeeCategory/created_fee_categories_form.html', context)
    else:
        user_form = fee_category_form()
        return render(request,'Dependencies/FeeCategory/fee_categories_form.html',{'user_form':user_form})


def edit_fee_category(request, fee_category_code):
    fee = get_object_or_404(Fee_Category, fee_category_code=fee_category_code)

    if request.method == "POST":
        user_form = fee_category_form(request.POST or None, instance=fee)
        if user_form.is_valid():
            user_form.save()
            return redirect('fee_category_list')
    else:
        user_form = fee_category_form(instance=fee)

        return render(request, 'Dependencies/FeeCategory/editfee.html', {'user_form': user_form})


def delete_fee_category(request, fee_category_code):
    Fee_Category.objects.filter(fee_category_code=fee_category_code).delete()
    fC = Fee_Category.objects.all()

    context = {
        'fees' : fC
    }
    return render(request, 'Dependencies/FeeCategory/list.html', context) 


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