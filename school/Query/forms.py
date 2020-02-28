from django import forms
from django.forms import ModelForm
from .models import Entry_data

class Form(forms.ModelForm):
    class Meta:
        model = Entry_data
        fields = {
            'Query_code',
            'Name',
            'father_name',
            'Address',
            'last',
            'Previous_school',
            'Addmission_required',
            'Test_performed',
            'Suggested_class',
            'test_teacher',
            'date_of_test',
            'Fee_type',
            'Contact',
        }