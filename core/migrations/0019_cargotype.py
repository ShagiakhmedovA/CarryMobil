# Generated by Django 3.1.4 on 2021-01-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210119_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50, verbose_name='Вид груза')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
        ),
    ]
