
from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'query/entry_test.html')

def form(request):
    return render(request, 'query/query_form.html')


def list(request):
    return render(request, 'query/query_list.html')


def detail(request):
    return render(request, 'query/query_detail.html')

