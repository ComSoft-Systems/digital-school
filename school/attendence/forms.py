from django import forms
from django.forms import ModelForm
from .models import *

class Attendence_Form(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(Attendence_Form, self).__init__(*args, **kwargs)
    #     self.fields['checkBox'].widget.attrs.update({
    #         'id': 'special',
    #     })
    class Meta:
        model = SelectAttendence
        fields = {
            'name', 
            'father',
            'classes', 
            'sections',
            'checkBox', 
        }
