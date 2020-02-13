from django.shortcuts import render , HttpResponse
from .models import Gr 
from .forms import ManageGrEntryForm 

def ManageGrListView(ListView):
    GrNumber = Gr.objects.all()
    return render (ListView,'Student/list.html',{'GrNumber':GrNumber})

def ManageGrCreateView(CreateView):
    # form = ManageGrEntryForm()
    # data = GrNumber.objects.create(gr_number = data['gr_number'],query_code = data['query_code'],name = data['name'],picture = data['picture'],family_code = data['family_code'],fee_catogery_code = data['fee_catogery_code'],class_of_admission = data['class_of_admission'],session_of_admission = data['session_of_admission'],current_class = data['current_class'],current_session = data['current_session'],admission_date = data['admission_date'],last_school = data['last_school'],religion = data['religion'])

    # GrNumber = Gr.objects.all()
    # if ListView.method == 'POST':
    #     form = ManageGrEntryForm(ListView.POST)
    #     if form.is_valid():
    #         order = form.save()
    #         for data in GrNumber:
    # else:
    #     form = ManageGrEntryForm()
    return render (CreateView,'Student/create.html')


def ManageGrDetailView(DetailView):
    model = None
    return render (DetailView, 'Student/detail.html')

