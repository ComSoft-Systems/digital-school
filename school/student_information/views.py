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
            # for item in Gr:
            #     OrderItem.objects.create( gr_number =['gr_number'] , query_code =['query_code'] , name =['name'] , picture =['picture'] , family_code =['family_code'] , fee_category_code =['fee_category_code'] , class_of_admission =['class_of_admission'] , session_of_admission =['session_of_admission'] , current_class =['current_class'] , current_session =['current_session'] , admission_date =['admission_date'] , last_school =['last_school'] , religion =['religion',] , date_of_birth =['date_of_birth'])
            # cart.clear()
            # order_created.delay(order.id)
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
