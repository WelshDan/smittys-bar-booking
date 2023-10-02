from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# user class for customer database #
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(required=True, unique=True, max_length=40)
    email = models.EmailField(max_length=100, unique=True, required=True)
    phone_number = PhoneNumberField(
        null=False, blank=False, unique=True, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
