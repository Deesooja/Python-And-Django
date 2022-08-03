from dataclasses import field
from pyexpat import model
from django import forms
from .models import registration

class Registrationform(forms.ModelForm):
    class Meta :
        model = registration 
        fields=['name','email','address']

widgets = {
   'name': forms.TextInput(attrs={'class':'form-control'}),
   'email': forms.EmailInput(attrs={'class':'form-control'}),
   'address': forms.TextInput( attrs={'class':'form-control'}),
  }