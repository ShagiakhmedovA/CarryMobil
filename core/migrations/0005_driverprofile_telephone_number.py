# Generated by Django 3.1.4 on 2021-06-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210615_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverprofile',
            name='telephone_number',
            field=models.CharField(blank=True, default=0, max_length=20, verbose_name='Номер телефона'),
        ),
    ]
