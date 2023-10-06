from django.db import models
from django.contrib.auth.models import User

class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=128)
    account_active = models.BooleanField(default=True)
