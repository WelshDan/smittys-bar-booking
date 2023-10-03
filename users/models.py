from django.db import models


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False,)
    password = models.CharField(max_length=50, blank=False)
    account_active = models.BooleanField()
