from django.shortcuts import render
from dependencies.models import *
from .forms import *


def ManageSmsView(SmsView):
    if SmsView.method == 'POST':
        Tool = SmsView.POST.get('tool')
        Clas = SmsView.POST.get('clas')
        Sms = SmsView.POST.get('sms')
        context = {
            'sms' : Sms,
            'tool' : Tool,
            'clas' : Clas,
        }
        if Tool == 'Sms':
            pass
        if Tool == 'WhatsApp':
            pass
        
        return render(SmsView , 'Sms/Create/created.html',context)
    else:
        data = Class.objects.all()
        context = {
            'data' : data
        }
        return render(SmsView , 'Sms/Create/create.html' , context)
