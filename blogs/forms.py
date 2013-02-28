__author__ = 'USer'

from django import forms
from django.forms import ModelForm
from blogs.models import Content


##class ContentForm(forms.Form):
##    post_title = forms.CharField(max_length=150)
##    post = forms.CharField(widget=forms.Textarea)

    #author = forms.CharField(max_length=50)

class ContentForm(ModelForm):
    class Meta:
        model=Content
        exclude=['author', 'blog_id', 'created_at']