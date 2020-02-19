from django.shortcuts import render , get_object_or_404 , HttpResponseRedirect
from .models import *
from .forms import *

def ManageGrListView(ListView):
    GrNumber = Gr.objects.all()
    context = {
        'GrNumber':GrNumber
    }
    return render (ListView,'Student/list.html',context)


def ManageGrCreateView(request):
    if request.method == 'POST':
        user_form = EntryForm(request.POST)
        if user_form.is_valid():
            form = user_form.save()
            return render(request,'Student/Create/created.html')
    else:
        user_form = EntryForm()
        return render(request,'Student/Create/create.html',{'user_form':user_form})

    

def ManageGrDetailView(DetailView,gr_number):
    GrNumber = get_object_or_404(Gr,gr_number = gr_number)
    context = {
        'GrNumber' : GrNumber,
    }
    return render (DetailView, 'Student/detail.html',context)
