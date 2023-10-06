# Generated by Django 3.2.21 on 2023-10-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20231006_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='customers',
            name='id',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='username',
        ),
        migrations.AddField(
            model_name='customers',
            name='account_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='email',
            field=models.CharField(default='dan.roberts78@gmail.com', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customers',
            name='first_name',
            field=models.CharField(default='default_first_name', max_length=50),
        ),
        migrations.AlterField(
            model_name='customers',
            name='last_name',
            field=models.CharField(default='default_last_name', max_length=50),
        ),
    ]
