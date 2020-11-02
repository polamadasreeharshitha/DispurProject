from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserRegisterForm(UserCreationForm):
    Address = forms.CharField()
    Email = forms.EmailField()
    Contact = forms.IntegerField()
    Date = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'Email', 'password1', 'password2','Address','Contact','Date']
