from django.shortcuts import render
from .forms import *

def ManageMainScreenView(request):
    return render(request, 'Main/Index.html')

def ManageLoginFormView(request):
    return render(request,'Main/LoginPage.html')

def ManageAboutView(request):
    return render(request,'Main/About.html')

def ManageSchoolView(request):
    return render(request,'Main/Schools.html')

def ManageContactView(request):
    return render(request,'Main/Contact.html')

def ManageTeamView(request):
    return render(request,'Main/Team.html')

def ManageDetailView(request):
    return render(request,'Main/Detail.html')

def ManageAfterLoginView(request):
    return render(request,'Admin/Common.html')

def ManageUserTypeView(ListView):
    return render(ListView,'User/UserType/List.html')

def ManageUserTypeCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = UserTypeForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'User/UserType/Created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'User/UserType/Created.html',context)
    else:
        user_form = UserTypeForm()
        context = {
                'form' : user_form
            }
        return render(CreateView,'User/UserType/Create.html',)

def ManageUserProfileView(ListView):
    return render(ListView,'User/UserProfile/List.html')

def ManageUserProfileCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = UserProfileForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'User/UserProfile/Created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'User/UserProfile/Created.html',context)
    else:
        user_form = UserProfileForm()
        context = {
                'form' : user_form
            }
        return render(CreateView,'User/UserProfile/Create.html',)