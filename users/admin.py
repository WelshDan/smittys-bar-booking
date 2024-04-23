from django.contrib import admin
from users.models import Customers

class customers(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'account_active')

admin.site.register(Customers, customers)