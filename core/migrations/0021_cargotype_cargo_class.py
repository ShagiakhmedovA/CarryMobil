# Generated by Django 3.1.4 on 2021-01-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210120_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargotype',
            name='cargo_class',
            field=models.CharField(default=0, max_length=50, verbose_name='Класс'),
            preserve_default=False,
        ),
    ]
