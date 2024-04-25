from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Customers

# Create a new user registration form

class RegisterForm(ModelForm):

    class Meta:
        model = Customers
        fields = ['email', 'password', 'first_name', 'last_name']

