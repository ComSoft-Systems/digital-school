from django.shortcuts import render , get_object_or_404 , HttpResponseRedirect ,redirect , get_list_or_404
from .models import *
from .forms import *
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
import csv, io
from django.contrib import messages


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

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
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

def ManageGrDeleteView(request, gr_number):
    Gr.objects.filter(gr_number=gr_number).delete()
    a = Gr.objects.all()
    return render(request, 'Student/Delete/delete.html')


def ManageGrUploadView(CreateView):
    format = {
        'order': 'Order of the CSV should be gr_number,query_code,name,picture,family_code,fee_concession_code,class_of_admission,session_of_admission,current_class,current_session,admission_date,last_school,religion,date_of_birth'
    }
    if CreateView.method == "GET":
        return render(CreateView,"Student/Create/ViaFile/create.html", format)
    InFile = CreateView.FILES['file']
    if not InFile.name.endswith('.csv'):
        messages.error(CreateView, 'This is not a csv file')
    data_set = InFile.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = EntryForm({
            'gr_number' : column[0] ,
            'query_code' : column[1] ,
            'name' : column[2] ,
            'picture' : column[3] ,
            'family_code' : column[4] ,
            'section' : column[5] ,
            'fee_concession_code' : column[6] ,
            'class_of_admission' : column[7] ,
            'session_of_admission' : column[8] ,
            'current_class' : column[9] ,
            'current_session' : column[10] ,
            'admission_date' : column[11] ,
            'last_school' : column[12] ,
            'religion' : column[13] ,
            'date_of_birth' : column[14],
            'active' : column[15],
            })
        created.save()
    context = {}
    return render(CreateView,"Student/Create/ViaFile/create.html", context)