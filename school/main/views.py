from django.shortcuts import render


def mainScreen(request):
    return render(request,'main/main.html')