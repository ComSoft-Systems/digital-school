from django.shortcuts import render , get_object_or_404 , HttpResponseRedirect ,redirect , get_list_or_404
from .models import *
from .forms import *
from django.views.generic.base import View


def ManageGrListView(ListView):
    GrNumber = Gr.objects.all()
    context = {
        'GrNumber':GrNumber
    }
    return render (ListView,'Student/list.html',context)

def ManageGrDetailView(DetailView,gr_number):
    GrNumber = get_object_or_404(Gr,gr_number = gr_number)
    context = {
        'GrNumber' : GrNumber,
    }
    return render (DetailView, 'Student/detail.html',context)

def ManageGrCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = EntryForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'Student/Create/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'Student/Create/created.html',context)
    else:
        user_form = EntryForm()
        return render(CreateView,'Student/Create/create.html',{'user_form':user_form})

def ManageGrEditView(request, gr_number):
    data = get_object_or_404(Gr, gr_number = gr_number)
    if request.method == "POST":
        user_form = EntryForm(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('gr_list')
    else:
        user_form = EntryForm(instance=data)
        return render(request, 'Student/Edit/edit.html',{'GrNumber':user_form,'data':data}) 




