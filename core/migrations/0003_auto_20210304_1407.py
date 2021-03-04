# Generated by Django 3.1.4 on 2021-03-04 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210304_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='author',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ID Автора'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 4, 14, 7, 10, 399313), null=True, verbose_name='Время отправки заявки'),
        ),
    ]
