# Generated by Django 4.2.9 on 2024-04-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_reservations_email_alter_reservations_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='booking_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]