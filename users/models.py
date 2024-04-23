from django.db import models
from django.contrib.auth.models import User

class Customers(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=100)
    account_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email