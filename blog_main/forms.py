__author__ = 'sasha'

from django import forms
from django.forms import ModelForm
from models import Blog


#class BlogForm (forms.Form):
#    name=forms.CharField(max_length=200)
#    description=forms.CharField(max_length=200)
#
#class RegistrationForm (forms.Form):
#    username=forms.CharField(max_length=200)
#    password=forms.CharField(widget=forms.PasswordInput(),max_length=10);
#    confirm=forms.CharField(widget=forms.PasswordInput(),max_length=10);



class BlogForm(ModelForm):
    class Meta:
        model=Blog
        exclude=['user','created_at']

##class BlogForm(ModelForm):
##    class Meta:
##        model=Blog,
##        exclude=['user','created_at']

#class BlogForm (forms.Form):
#    blog_title = forms.CharField(max_length=150)
#    blog_description = forms.CharField(widget=forms.Textarea)
#    blog_tags = forms.CharField(max_length=255)


