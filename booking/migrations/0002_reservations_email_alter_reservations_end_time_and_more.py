# Generated by Django 4.2.9 on 2024-04-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='email',
            field=models.CharField(default=''),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='end_time',
            field=models.TimeField(default=4),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='start_time',
            field=models.TimeField(default=4),
        ),
    ]