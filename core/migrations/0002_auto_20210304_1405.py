# Generated by Django 3.1.4 on 2021-03-04 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 4, 14, 5, 37, 917591), null=True, verbose_name='Время отправки заявки'),
        ),
    ]
