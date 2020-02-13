from django.shortcuts import render


def LoginForm(request):
    return render(request,'LoginPage.html')

def MainScreen(request):
    return render(request, 'MainPage.html')