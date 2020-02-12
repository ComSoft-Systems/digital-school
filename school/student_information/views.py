from django.shortcuts import render , HttpResponse
from .models import Gr , Family
from .forms import ManageGrListForm 

def ManageGrListView(ListView):
    GrNumber = Gr.objects.all()
    return render (ListView,'Student/list.html',{'GrNumber':GrNumber})
    
def ManageGrDetailView(DetailView):
    model = None
    return render (DetailView, 'Student/detail.html')

def ManageFamilyListView(ListView):
    model = None
    return render (ListView,'Family/list.html')

def ManageFamilyDetailView(DetailView):
    model = None
    return render (DetailView,'Family/list.html')

