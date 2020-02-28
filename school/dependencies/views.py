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
    context = {'clas': clas}
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


def edit_class(request, pk):
    clas = get_object_or_404(Class, pk=pk)

    if request.method == "POST":
        user_form = class_form(request.POST or None, instance=clas)
        if user_form.is_valid():
            user_form.save()
            return redirect('class_list')
    else:
        user_form = class_form(instance=clas)

        return render(request, 'Dependencies/Classes/editclass.html', {'user_form': user_form}) 


def school_list(request):
    schol = School.objects.all()
    context = {'schol': schol}
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


def family_list(request):
    fami = Family.objects.all()
    context = {'fami': fami}
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


def fee_category_list(request):
    fee = Fee_Category.objects.all()
    context = {'fee': fee}
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


def section_list(request):
    sec = Section.objects.all()
    context = {'sec': sec}
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
            


def session_list(request):
    sess = Session.objects.all()
    context = {'sess': sess}
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

    

def religion_list(request):
    reli = Religion.objects.all()
    context = {'reli': reli}
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