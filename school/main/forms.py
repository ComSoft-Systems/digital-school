from django import forms
from django.forms import ModelForm
from .models import *


class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = [
            'TypeCode',
            'UserType',
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'UserCode',
            'UserType',
            'Name',
            'Father',
            'Address' ,
            'Mobile',
            'Email',
            'Password',
        ]