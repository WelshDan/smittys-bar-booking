from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number',
                  'password1', 'password2')
