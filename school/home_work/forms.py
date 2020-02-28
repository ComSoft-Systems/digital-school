from django import forms
from django.forms import ModelForm
from .models import home_work

class home_work(forms.ModelForm):
    class Meta:
        model = home_work
        fields = {
            'homework_ID', 
            'classes', 
            'sections', 
            'teacher',
            'subjects', 
            'chapter', 
            'page', 
            'descriptions'
        }