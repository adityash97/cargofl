# Generated by Django 3.2.4 on 2022-06-16 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_alternate_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]