from django import forms
from app.models import *

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

class ChinniBFListForm(forms.ModelForm):
    class Meta:
        model=ChinniBFList
        fields='__all__'