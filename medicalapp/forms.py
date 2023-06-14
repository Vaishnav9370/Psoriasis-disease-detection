from django import forms
from .models import *

class regform(forms.ModelForm):
    class Meta:
        model=regmodel
        fields=('fname','email','password','phoneNumber','gen','adrs','District')
        widigets={
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control'}),
            'gen':forms.TextInput(attrs={'class':'form-control'}),
            'adrs':forms.TextInput(attrs={'class':'form-control'}),
            'District':forms.TextInput(attrs={'class':'form-control'}),
        }
