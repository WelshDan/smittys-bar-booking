from django.db import models
from django.contrib.auth.models import User

class Customers(models.Model):

    def __str__(self):
        return self.name