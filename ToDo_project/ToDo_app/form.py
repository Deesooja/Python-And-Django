from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import All_todo

class All_todo_form(forms.ModelForm):
    class Meta:
        model = All_todo
        fields = ['todo']
        
    
widgets = {
   'todo': forms.TextInput(attrs={'class':'form-control'}),
   
  }

