# Generated by Django 4.1.1 on 2022-10-10 18:54

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_delete_customers_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(default=base.models.some_time),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
