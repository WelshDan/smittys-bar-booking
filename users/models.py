from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models
from django.utils import timezone


class CustomersManager(BaseUserManager):
    # Define Base User
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Please enter email")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Define Superuser
    def create_superuser(self, email, password=None):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValeuError("Superuser must have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email, password)


class Customers(AbstractBaseUser, PermissionsMixin):
    # Model for signing in new users
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    account_active = models.BooleanField(default=True)
    # Extra information
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomersManager()

    # Define what is the main field is
    def __unicode__(self):
        return self.email

    REQUIRED_FIELDS = ('id', 'first_name', 'last_name', 'password1')
    USERNAME_FIELD = ('email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
