# Generated by Django 4.2.9 on 2024-04-23 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customers_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='user',
        ),
    ]
