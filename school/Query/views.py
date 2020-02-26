from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Entry_data
from .forms import Form

def home(request):
    return render(request, 'query/entry_test.html')

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
    

def list(request):
    return render(request, 'query/query_list.html')


def detail(request):
    return render(request, 'query/query_detail.html')