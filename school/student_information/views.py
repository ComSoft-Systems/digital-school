from django.shortcuts import render,HttpResponse
from .models import *

def ManageGrListView(ListView):
    model = None
    return render (ListView,'Student/list.html')
    
def ManageGrDetailView(DetailView):
    model = None
    return render (DetailView, 'Student/detail.html')

def ManageFamilyListView(ListView):
    model = None
    return render (ListView,'Family/list.html')

def ManageFamilyDetailView(DetailView):
    model = None
    return render (DetailView,'Family/list.html')

