from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def home_work_info(CreateView):
    
    if CreateView.method == 'POST':
        user_form = home_work(CreateView.POST)
        
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'home_work/Create/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            } 
            return render(CreateView,'home_work/Create/created.html',context)

    else:
        user_form = home_work()
        return render(CreateView,'home_work/Create/create.html',{'user_form':user_form})