from django.shortcuts import render

def MainScreen(request):
    return render(request, 'index.html')

def LoginForm(request):
    return render(request,'LoginPage.html')

def about(request):
    return render(request,'about.html')

def school(request):
    return render(request,'schools.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

def detail(request):
    return render(request,'detail.html')

def afterlogin(request):
    return render(request,'main.html')