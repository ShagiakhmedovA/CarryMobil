# Generated by Django 3.1.4 on 2021-05-17 03:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20210511_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complitedorder',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 17, 6, 30, 26, 258840), null=True, verbose_name='Время отправки заявки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 17, 6, 30, 26, 258840), null=True, verbose_name='Время отправки заявки'),
        ),
        migrations.AlterField(
            model_name='telorder',
            name='sended_in',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 17, 6, 30, 26, 274466), null=True, verbose_name='Время отправки заявки'),
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_series', models.CharField(blank=True, max_length=4, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(blank=True, max_length=6, verbose_name='Номер паспорта')),
                ('driver_licenses_series', models.CharField(blank=True, max_length=4, verbose_name='Серия водительского удостоверения')),
                ('driver_licenses_number', models.CharField(blank=True, max_length=6, verbose_name='Номер водительского удостоверения')),
                ('complited_orders', models.CharField(blank=True, max_length=40, verbose_name='Завершенные заказы')),
                ('canceled_orders', models.CharField(blank=True, max_length=40, verbose_name='Отмененные заказы')),
                ('driver_rating', models.CharField(blank=True, max_length=40, verbose_name='Рейтинг водителя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
