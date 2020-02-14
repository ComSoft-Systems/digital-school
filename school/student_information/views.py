from django.shortcuts import render , get_object_or_404
from .models import *
from .forms import ManageGrEntryForm 

def ManageGrListView(ListView):
    GrNumber = Gr.objects.all()
    context = {
        'GrNumber':GrNumber
    }
    return render (ListView,'Student/list.html',context)

def ManageGrCreateView(request):
    form = ManageGrEntryForm()
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render (request,'Student/create.html',context)

def ManageGrDetailView(DetailView,gr_number):
    GrNumber = get_object_or_404(Gr,gr_number = gr_number)
    Grnumber = gr_number
    if GrNumber == Grnumber :
        context = {
            'GrNumber' : GrNumber,
        }
        return render (DetailView, 'Student/detail.html',context)
    else:
        context = {
            'GrNumber' : "Not Found",
        }
        return render (DetailView, 'Student/detail.html',context)
