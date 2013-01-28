__author__ = 'sasha'

from django import forms
from django.forms import ModelForm
from models import User


class LoginForm (forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput(),max_length=10);

class RegistrationForm (forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput(),max_length=10);
    confirm=forms.CharField(widget=forms.PasswordInput(),max_length=10);


class ProfileForm(ModelForm):
    class Meta:
        model=User
        exclude=['user',]
