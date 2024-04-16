# Generated by Django 4.2.9 on 2024-04-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_reservations_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='active_booking',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='end_time',
            field=models.TimeField(default=23),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='start_time',
            field=models.TimeField(default=23),
        ),
    ]
