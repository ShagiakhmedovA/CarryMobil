# Generated by Django 3.2 on 2021-06-13 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='AssistantLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(blank=True, max_length=150, verbose_name='Ответ пользователя')),
                ('assistant_text', models.TextField(blank=True, verbose_name='Текст ассистента')),
                ('function_id', models.IntegerField(blank=True, default=0, null=True, verbose_name='Функция')),
            ],
            options={
                'verbose_name': 'Ответ ассистента',
                'verbose_name_plural': 'Словарь ассистента',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Марка')),
                ('car_model', models.CharField(blank=True, max_length=50, null=True, verbose_name='Модель')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('registration_number', models.CharField(max_length=9, verbose_name='Регистрационные номера')),
                ('length', models.CharField(max_length=4, verbose_name='Длина')),
                ('height', models.CharField(max_length=4, verbose_name='Высота')),
                ('width', models.CharField(max_length=4, verbose_name='Ширина')),
                ('volume', models.CharField(max_length=4, verbose_name='Объём')),
                ('tonnage', models.CharField(max_length=4, verbose_name='Тоннаж')),
            ],
        ),
        migrations.CreateModel(
            name='CargoType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=50, verbose_name='Вид груза')),
                ('cargo_class', models.CharField(blank=True, max_length=50, null=True, verbose_name='Класс')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Вид груза',
                'verbose_name_plural': 'Виды грузов',
            },
        ),
        migrations.CreateModel(
            name='CityPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_1', models.CharField(max_length=150, verbose_name='Город 1')),
                ('city_2', models.CharField(max_length=150, verbose_name='Город 2')),
                ('distance', models.IntegerField(verbose_name='Расстояние')),
                ('price_1_5t', models.IntegerField(verbose_name='Стоимость до 1.5 тонн')),
                ('price_3t', models.IntegerField(verbose_name='Стоимость до 3 тонн')),
                ('price_5t', models.IntegerField(verbose_name='Стоимость до 5 тонн')),
            ],
        ),
        migrations.CreateModel(
            name='ComplitedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_road', models.CharField(max_length=1500, verbose_name='Маршрут')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Время прибытия на заказ')),
                ('road_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к доргоге')),
                ('cargo_type', models.CharField(blank=True, max_length=60, verbose_name='Тип груза')),
                ('cargo_type_comment', models.TextField(blank=True, null=True, verbose_name='Тип груза комментарий')),
                ('loader_count', models.IntegerField(blank=True, null=True, verbose_name='Количество грузчиков')),
                ('loader_time_count', models.IntegerField(blank=True, null=True, verbose_name='Количество часов для грузчиков')),
                ('order_price', models.IntegerField(verbose_name='Стоимость заказа')),
                ('prices', models.CharField(blank=True, max_length=150, null=True, verbose_name='Цены заказа')),
                ('user_tel_nomer', models.CharField(max_length=20, verbose_name='Номер телефона заказчика')),
                ('sended_in', models.DateTimeField(blank=True, null=True, verbose_name='Время отправки заявки')),
                ('status', models.IntegerField(blank=True, default=0, null=True, verbose_name='Состояние заказа')),
                ('author', models.IntegerField(blank=True, default=0, null=True, verbose_name='ID Автора')),
            ],
            options={
                'verbose_name': 'Завершенный заказ',
                'verbose_name_plural': 'Завершенные заказы',
            },
        ),
        migrations.CreateModel(
            name='DispatcherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_series', models.IntegerField(max_length=4, verbose_name='Серия паспорта')),
                ('passport_number', models.IntegerField(max_length=6, verbose_name='Номер паспорта')),
                ('registration_address', models.IntegerField(max_length=250, verbose_name='Адрес прописки')),
                ('complited_orders', models.IntegerField(blank=True, max_length=40, verbose_name='Завершенные заказы')),
                ('canceled_orders', models.IntegerField(blank=True, max_length=40, verbose_name='Отмененные заказы')),
                ('dispatcher_rating', models.IntegerField(blank=True, default=0, max_length=40, verbose_name='Рейтинг Диспетчера')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_series', models.CharField(max_length=4, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(max_length=6, verbose_name='Номер паспорта')),
                ('driver_licenses_series', models.CharField(max_length=4, verbose_name='Серия водительского удостоверения')),
                ('driver_licenses_number', models.CharField(max_length=6, verbose_name='Номер водительского удостоверения')),
                ('registration_address', models.CharField(max_length=250, verbose_name='Адрес прописки')),
                ('complited_orders', models.CharField(blank=True, max_length=40, verbose_name='Завершенные заказы')),
                ('canceled_orders', models.CharField(blank=True, max_length=40, verbose_name='Отмененные заказы')),
                ('driver_rating', models.CharField(blank=True, default=0, max_length=40, verbose_name='Рейтинг водителя')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.car')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TelOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя заказчика')),
                ('user_tel_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('sended_in', models.DateTimeField(blank=True, null=True, verbose_name='Время отправки заявки')),
                ('author', models.IntegerField(blank=True, default=0, null=True, verbose_name='ID Автора')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.IntegerField(blank=True, default=1, null=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=50)),
                ('company', models.CharField(blank=True, max_length=40)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('telephone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_road', models.CharField(max_length=1500, verbose_name='Маршрут')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='Время прибытия на заказ')),
                ('road_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к доргоге')),
                ('cargo_type', models.CharField(blank=True, max_length=60, verbose_name='Тип груза')),
                ('cargo_type_comment', models.TextField(blank=True, null=True, verbose_name='Тип груза комментарий')),
                ('loader_count', models.IntegerField(blank=True, null=True, verbose_name='Количество грузчиков')),
                ('loader_time_count', models.IntegerField(blank=True, null=True, verbose_name='Количество часов для грузчиков')),
                ('order_price', models.IntegerField(verbose_name='Стоимость заказа')),
                ('prices', models.CharField(blank=True, max_length=150, null=True, verbose_name='Цены заказа')),
                ('user_tel_nomer', models.CharField(max_length=20, verbose_name='Номер телефона заказчика')),
                ('sended_in', models.DateTimeField(blank=True, null=True, verbose_name='Время отправки заявки')),
                ('status', models.IntegerField(blank=True, default=0, null=True, verbose_name='Состояние заказа')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('dispatcher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dispatcher', to='core.dispatcherprofile', verbose_name='dispatcher')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='core.driverprofile', verbose_name='driver')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=50, verbose_name='Вид деятельности')),
                ('passport_series', models.CharField(max_length=4, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(max_length=6, verbose_name='Номер паспорта')),
                ('registration_address', models.CharField(max_length=250, verbose_name='Адресс прописки')),
                ('driver_licenses_series', models.CharField(blank=True, max_length=4, verbose_name='Серия водительского удостоверения')),
                ('driver_licenses_number', models.CharField(blank=True, max_length=6, verbose_name='Номер водительского удостоверения')),
                ('telephone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
