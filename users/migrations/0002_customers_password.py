# Generated by Django 4.2.9 on 2024-04-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='password',
            field=models.CharField(default='password', max_length=128),
        ),
    ]
