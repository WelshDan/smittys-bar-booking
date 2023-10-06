from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Customers

# Create a new user registration form


class RegisterForm(ModelForm):
    emails = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)

    class Meta:
        model = Customers
        fields = ['first_name',
                  'last_name', 'emails', 'password']

