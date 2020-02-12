from django.shortcuts import render

def ManageClassesListView(ListView):
    model = None
    return render (ListView,'Dependencies/Classes/list.html')

def ManageClassesDetailView(DetailView):
    model = None
    return render (DetailView,'Dependencies/Classes/list.html')


def ManageSchoolsListView(ListView):
    model = None
    return render (ListView,'Dependencies/Schools/list.html')

def ManageSchoolsDetailView(DetailView):
    model = None
    return render (DetailView,'Dependencies/Schools/list.html')

def ManageFeeCategoryListView(ListView):
    model = None
    return render (ListView,'Dependencies/FeesCategory/list.html')

def ManageFeeCategoryDetailView(DetailView):
    model = None
    return render (DetailView,'Dependencies/FeesCategory/list.html')

def section(request):
    return render(request, 'Dependencies/section.html')

def session(request):
    return render(request, 'Dependencies/session.html')

def ManageFamilyListView(ListView):
    model = None
    return render (ListView,'Dependencies/Family/list.html')

def ManageFamilyDetailView(DetailView):
    model = None
    return render (DetailView,'Dependencies/Family/list.html')