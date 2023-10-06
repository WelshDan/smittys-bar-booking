from django.db import models
from django.contrib.auth.models import User

class Customers(models.Model):
    first_name = models.CharField(max_length=50, default='default_first_name')
    last_name = models.CharField(max_length=50, default='default_last_name')
    email = models.CharField(primary_key=True, max_length=100, default='dan.roberts78@gmail.com')
    password = models.CharField(max_length=128, default='default_password')
    account_active = models.BooleanField(default=True)
