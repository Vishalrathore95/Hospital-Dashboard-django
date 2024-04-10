# forms.py

from django import forms
from doctorlogin.models import Doctor

class UserProfileForm(forms.ModelForm):
    class Meta:
        model =  Doctor
        fields = ['profile_picture']
