from django.shortcuts import render , redirect , get_object_or_404
from .forms import *
from .models import *
from dependencies.forms import *
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
import datetime



@login_required(login_url='login_url')
def ManageFeeTypeListView(ListView):
    fee = ClassFee.objects.all()
    context = {
        'fee':fee
    }
    return render (ListView,'ClassFee/list.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeTypeCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = ClassFeeForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'ClassFee/Create/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'ClassFee/Create/created.html',context)
    else:
        user_form = ClassFeeForm()
        return render(CreateView,'ClassFee/Create/create.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeTypeEditView(request, fee_type_code):
    data = get_object_or_404(ClassFee, fee_type_code = fee_type_code)
    if request.method == "POST":
        user_form = ClassFeeForm(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('class_fee_list')
    else:
        user_form = ClassFeeForm(instance=data)
        return render(request, 'ClassFee/Edit/edit.html',{'user_form':user_form,'data':data}) 

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeTypeDeleteView(request, fee_type_code):
    ClassFee.objects.filter(fee_type_code=fee_type_code).delete()
    a = ClassFee.objects.all()
    return render(request, 'ClassFee/Delete/delete.html')





@login_required(login_url='login_url')
def ManageFeeDefListView(ListView):
    fee = StFeeDefine.objects.all()
    context = {
        'fee':fee
    }
    return render (ListView,'FeesDefine/list.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeDefCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = FeeDefineForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'FeesDefine/Create/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'FeesDefine/Create/created.html',context)
    else:
        user_form = FeeDefineForm()
        return render(CreateView,'FeesDefine/Create/create.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeDefEditView(request, fee_def_code):
    data = get_object_or_404(StFeeDefine, fee_def_code = fee_def_code)
    if request.method == "POST":
        user_form = FeeDefineForm(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('fee_def_list')
    else:
        user_form = FeeDefineForm(instance=data)
        return render(request, 'FeesDefine/Edit/edit.html',{'user_form':user_form,'data':data}) 

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeDefDeleteView(request, fee_def_code):
    StFeeDefine.objects.filter(fee_def_code=fee_def_code).delete()
    a = StFeeDefine.objects.all()
    return render(request, 'FeesDefine/Delete/delete.html')





@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeRegisterListView(ListView):
    fee = FeeRegister.objects.all()
    context = {
        'fee':fee
    }
    return render (ListView,'FeesRegister/list.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeRegisterDetailView(DetailView,fee_reg_id):
    fee = get_object_or_404(FeeRegister,fee_reg_id = fee_reg_id)
    context = {
        'fee' : fee,
    }
    return render (DetailView, 'FeesRegister/detail.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeRegisterCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = FeeRegisterForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'FeesRegister/Create/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'FeesRegister/Create/created.html',context)
    else:
        user_form = FeeRegisterForm()
        return render(CreateView,'FeesRegister/Create/create.html',{'user_form':user_form})

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeRegisterCreateToAllView(CreateView):
    if CreateView.method == 'POST':
        clas = CreateView.POST.get('class_code')
        fee_type = CreateView.POST.get('fee_type_code')
        startmonth = CreateView.POST.get('month')
        duedate = CreateView.POST.get('date')
        v = 8
        for gr_row in Gr.objects.all():
            gr_rows = gr_row
            for std_fee_rows in StFeeDefine.objects.all():
                st_fe_def_rows = std_fee_rows
                for feerows in ClassFee.objects.all():
                    fee_type_rows = feerows
                    for cla_rows in Class.objects.all():
                        class_rows = cla_rows
                        for feetyperows in Fee_Type.objects.all():
                            feerows = feetyperows
                            if str(gr_rows.name) == str(st_fe_def_rows.gr_number):
                                if str(class_rows.class_code) == clas:
                                    class_ = class_rows.class_name
                                    if str(feerows.fee_type_code) == fee_type:
                                        feetype = feerows.fee_type
                                        if str(gr_rows.current_class) == str(class_):
                                            if str(feerows.fee_type) == feetype:
                                                formfill = FeeRegister(
                                                    int(v) ,
                                                    gr_rows.gr_number ,
                                                    feerows.fee_type_code ,
                                                    int(fee_type_rows.fee_amount)-(int(fee_type_rows.fee_amount)*(st_fe_def_rows.concession_percent)/100) ,
                                                    startmonth ,
                                                    duedate ,
                                                    '0' ,
                                                    )
                                                v = v+1
                                                formfill.save()
                                                context = {'return' : 'Has Been Added SuccessFully'}
        return render(CreateView,'FeesRegister/Create/ToAll/created.html',context)
    else:
        class_ = ClassFeeForm()
        fee_type = ClassFeeForm()
        month = FeeRegisterForm()
        date_form = DateForm()
        context = {
            'a' : class_,
            'b' : fee_type,
            'c' : month,
            'd' : date_form,
        }
        return render(CreateView,'FeesRegister/Create/ToAll/create.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeRegisterEditView(request, fee_reg_id):
    data = get_object_or_404(FeeRegister, fee_reg_id = fee_reg_id)
    if request.method == "POST":
        user_form = FeeRegisterForm(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('fee_def_list')
    else:
        user_form = FeeRegisterForm(instance=data)
        return render(request, 'FeesRegister/Edit/edit.html',{'user_form':user_form,'data':data}) 

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageFeeRegisterDeleteView(request, fee_reg_id):
    FeeRegister.objects.filter(fee_reg_id=fee_reg_id).delete()
    a = FeeRegister.objects.all()
    return render(request, 'FeesRegister/Delete/delete.html')


