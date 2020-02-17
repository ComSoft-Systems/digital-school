from django.shortcuts import render

def MainScreen(request):
    return render(request, 'index.html')

def LoginForm(request):
    return render(request,'LoginPage.html')