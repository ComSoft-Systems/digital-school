from django.shortcuts import render

# Create your views here.
def classes(request):
    return render(request, 'dependencies/classes.html')

def schools(request):
    return render(request, 'dependencies/schools.html')

def fee_category(request):
    return render(request, 'dependencies/fee_category.html')

def section(request):
    return render(request, 'dependencies/section.html')

def session(request):
    return render(request, 'dependencies/session.html')

def family(request):
    return render(request, 'dependencies/family.html')