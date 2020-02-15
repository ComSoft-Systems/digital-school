from django.shortcuts import render , get_object_or_404 , HttpResponseRedirect
from .models import *
from .forms import ManageGrEntryForm 

def ManageGrListView(ListView):
    GrNumber = Gr.objects.all()
    context = {
        'GrNumber':GrNumber
    }
    return render (ListView,'Student/list.html',context)


def ManageGrCreateView(request):
    if request.method == 'POST':
        user_form = ManageGrEntryForm(request)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('ManageGrListView'))
        else:
            context ={
                'gr_number':gr_number,
                'query_code':query_code,
            }
            return render(request,'Student/create.html',{'user_form':user_form})
    else:
        user_form = ManageGrEntryForm()
        return render(request,'Student/create.html',{'user_form':user_form})

    

def ManageGrDetailView(DetailView,gr_number):
    GrNumber = get_object_or_404(Gr,gr_number = gr_number)
# Grnumber = gr_number
# if GrNumber == gr_number :
    context = {
        'GrNumber' : GrNumber,
    }
    return render (DetailView, 'Student/detail.html',context)
# else:
    # context = {
    #     'GrNumber' : "Not Found",
    # }
    # return render (DetailView, 'Student/detail.html',context)
