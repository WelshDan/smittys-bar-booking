from django.db import models


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, unique=True)
    account_active = models.BooleanField(default=True)

    def __str__(self):
        return ('first_name' + ' ' + 'last_name')
