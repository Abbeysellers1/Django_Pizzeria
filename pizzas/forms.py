from .models import *
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('name', 'text')
        labels={'name': 'name', 'text': ''}


        