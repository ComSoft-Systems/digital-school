from django import forms
from django.forms import ModelForm
from .models import Exam , Semester, Semesterbreakup

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = {
            'exam_code',
            'exam_session'
        }
        
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = {
            'exam_code',
            'semester_code',
            'semester_name'
        }

class SemesterbreakupForm(forms.ModelForm):
    class Meta:
        model = Semesterbreakup
        fields = {
            'exam_code',
            'semester_code',
            'semesterbreakup_code',
            'semesterbreakup_name'
        }
        