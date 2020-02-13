from django.shortcuts import render
from .models import Gr 
from .forms import ManageGrEntryForm 

def ManageGrListView(ListView):
    GrNumber = Gr.objects.all()
    context = {
        'GrNumber':GrNumber
    }
    return render (ListView,'Student/list.html',context)

def ManageGrCreateView(request):
    form = ManageGrEntryForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render (request,'Student/create.html',context)

def ManageGrDetailView(DetailView):
    model = None
    return render (DetailView, 'Student/detail.html')

