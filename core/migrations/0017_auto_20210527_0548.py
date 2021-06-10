# Generated by Django 3.1.4 on 2021-05-27 02:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0016_auto_20210524_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='DriverProfile', to='auth.user', verbose_name='driver'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complitedorder',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 27, 5, 48, 26, 797600), null=True, verbose_name='Время отправки заявки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 27, 5, 48, 26, 795555), null=True, verbose_name='Время отправки заявки'),
        ),
        migrations.AlterField(
            model_name='telorder',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 27, 5, 48, 26, 805672), null=True, verbose_name='Время отправки заявки'),
        ),
    ]
