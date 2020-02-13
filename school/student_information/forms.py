from django import forms
from .models import Gr

class ManageGrEntryForm(forms.Form):
    class meta:
        model = Gr
        fields = [
            'gr_number',
            'query_code',
            'name',
            'picture',
            'family_code',
            'fee_category_code',
            'class_of_admission',
            'session_of_admission',
            'current_class',
            'current_session',
            'admission_date',
            'last_school',
            'religion',
        ]


