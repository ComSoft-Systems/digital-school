
from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Entry_data

def home(request):
    return render(request, 'query/entry_test.html')

def form(request):
    return render(request, 'query/query_form.html')


def list(request):
    return render(request, 'query/query_list.html')


def detail(request):
    return render(request, 'query/query_detail.html')

def Entry_data_list(request):
    Entry_datas = Entry_data.published.all()
    return render(request,
    'Entry_data/list.html',
    {'Entry_datas':Entry_datas})


def	Entry_data_detail(request,Name ,father,last,Address):
    Entry_data = get_object_or_404(Entry_data, slug=Entry_data,
                                               father='published',
                                               publish_Name=Name,
                                               publish_last=last,
                                               publish_Address=Address)
    return render(request,
	        'Entry_data/detail.html',
            {'Entry_data':Entry_data})