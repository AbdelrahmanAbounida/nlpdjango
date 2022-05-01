from dataclasses import field
from tkinter import Widget
from tkinter.ttk import Style
from django.forms import CharField, ModelForm, Textarea,TextInput,BooleanField
from .models import Choices

class ChoicesForm(ModelForm):
    api_tocken = TextInput(attrs={'class':'form-control'})
    language = TextInput()
    model = TextInput(attrs={'class':'form-control','aria-describedby':"emailHelp"})
    use_gpu = BooleanField()
    question = CharField(widget=Textarea(attrs={'class': 'form-control mx-auto', 'placeholder': 'Text goes here', 'rows': '4', 'cols': '143'}))
    inpt_string = CharField(widget=Textarea(attrs={'class': 'form-control mx-auto', 'placeholder': 'Write a Question', 'rows': '6', 'cols': '143'}))


    class Meta:
        model = Choices
        fields = ['api_tocken','language','model','use_gpu','question','inpt_string']

