from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customers

# Create a new user registration form


class RegisterForm(UserCreationForm):

    class Meta:
        model = Customers
        fields = ('id', 'first_name',
                  'last_name', 'email', 'password1', 'password2')
