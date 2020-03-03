from django import forms
from django.forms import ModelForm
from .models import Class, School, Family, Fee_Category, Section, Session, Religion, Subject

class class_form(forms.ModelForm):
    class Meta:
        model = Class
        fields = {
            'class_code',
            'class_name',
            'remarks'
        }

class school_form(forms.ModelForm):
    class Meta:
        model = School
        fields = {
            'school_code',
            'school_name',
            'school_area',
            'remarks'
        }

class family_form(forms.ModelForm):
    class Meta:
        model = Family
        fields = {
            'family_code',
            'surname',
            'father_name',
            'ph_no_father',
            'mother_name',
            'ph_no_mother',
            'address'
        }

class fee_category_form(forms.ModelForm):
    class Meta:
        model = Fee_Category
        fields = {
            'fee_category_code',
            'fee_category_name',
            'percent',
            'amount'
        }

class section_form(forms.ModelForm):
    class Meta:
        model = Section
        fields = {
            'sect_code',
            'sect_name',
            'remarks'
        }

class session_form(forms.ModelForm):
    class Meta:
        model = Session
        fields = {
            'session_code',
            'session_name'
        }

class religion_form(forms.ModelForm):
    class Meta:
        model = Religion
        fields = {
            'religion_code',
            'religion'
        }


class subject_form(forms.ModelForm):
    class Meta:
        model = Subject
        fields = {
            'subject_code',
            'subjects'
        }