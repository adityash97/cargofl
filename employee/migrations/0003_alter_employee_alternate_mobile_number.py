# Generated by Django 3.2.4 on 2022-06-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220616_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='alternate_mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
