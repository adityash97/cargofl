# Generated by Django 3.2.4 on 2022-06-17 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_employee_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
