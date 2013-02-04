__author__ = 'USer'

from django import forms
from django.forms import ModelForm


class ContentForm(forms.Form):
    post_title = forms.CharField(max_length=150)
    post = forms.CharField(widget=forms.Textarea)

    #author = forms.CharField(max_length=50)