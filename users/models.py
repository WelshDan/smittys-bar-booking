from django.db import models
from django.contrib.auth.models import User


class Customers(models.Model):
    email = models.EmailField(
        max_length=100, blank=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    account_active = models.BooleanField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
