from django.shortcuts import render,redirect, get_object_or_404
from .models import Entry_data
from .forms import Form
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .filters import Entry_dataFilter


def home(request):
    return render(request, 'query/entry_test.html')

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def form(request):
    if request.method == 'POST':
        user_form = Form(request.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'Query/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'Query/created.html',context)
    else:
        user_form = Form()
        return render(request,'Query/Query_form.html',{'user_form':user_form})


def detail(request,Query_code):
    abc = get_object_or_404(Entry_data,Query_code = Query_code)
    context = {
        'Entry': abc,
    }
    return render(request, 'query/query_detail.html', context)

@login_required(login_url='login_url')
def list_view(request):
    Entry_dataa = Entry_data.objects.all()
    myFilter = Entry_dataFilter(request.GET, queryset = Entry_dataa)
    Entry_dataa = myFilter.queryset 
    context = {'Entry': Entry_dataa, 'myFilter': myFilter }
    return render (request,'query/query_list.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def edit(request,Query_code):
    i = get_object_or_404(Entry_data, Query_code=Query_code)
    if request.method == "POST":
        user_form = Form(request.POST, instance=i)
        if user_form.is_valid():
            user_form.save()
            return redirect('list_view')
    else:
        user_form = Form(instance=i)
        return render(request, 'query/edit_query.html', {'user_form':user_form})
    
@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def delete(request, Query_code):
    Entry_data.objects.filter(Query_code=Query_code).delete()
    a = Entry_data.objects.all()

    context = {
        'Entry' : a
    }
    return render(request, 'query/query_list.html', context)