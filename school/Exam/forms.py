from django import forms
from django.forms import ModelForm
from .models import *

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = {
            'exam_code',
            'exam_session'
        }
        
