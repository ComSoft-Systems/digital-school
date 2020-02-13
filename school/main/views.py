from django.shortcuts import render


def mainScreen(request):
    return render(request,'LoginPage.html')