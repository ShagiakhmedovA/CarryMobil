from django.db import models


class Order(models.Model):
    from_address = models.CharField('Откуда', max_length=150)
    to_address = models.CharField('Куда', max_length=150)
    start_time = models.DateTimeField('Время прибытия на заказ', null=True, blank=True)
    road_comment = models.TextField('Комментарий к доргоге', null=True, blank=True)
    cargo_type = models.CharField('Тип груза', max_length=50, blank=True)
    cargo_type_comment = models.TextField('Тип груза комментарий', null=True, blank=True)
    loader_count = models.IntegerField('Количество грузчиков', null=True, blank=True)
    loader_time_count = models.IntegerField('Количество часов для грузчиков', null=True, blank=True)
    order_price = models.IntegerField('Стоимость заказа')
    user_tel_nomer = models.CharField('Номер телефона заказчика', max_length=20)
    status = models.IntegerField('Состояние заказа', null=True, blank=True)

    def __str__(self):
        return self.from_address

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Address(models.Model):
    address = models.CharField('Адрес', max_length=150,blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class CityPrice(models.Model):
    city_1 = models.CharField('Город 1', max_length=150)
    city_2 = models.CharField('Город 2', max_length=150)
    distance = models.IntegerField('Расстояние')
    price_1_5t = models.IntegerField('Стоимость до 1.5 тонн')
    price_3t = models.IntegerField('Стоимость до 3 тонн')
    price_5t = models.IntegerField('Стоимость до 5 тонн')

    def __str__(self):
        return self.city_1 + ' - ' + self.city_2


class CargoType(models.Model):
    cargo = models.CharField('Вид груза', max_length=50)
    cargo_class = models.CharField('Класс', max_length=50, null=True,blank=True)
    price = models.IntegerField('Стоимость')

    def __str__(self):
        return self.cargo

    class Meta:
        verbose_name = 'Вид груза'
        verbose_name_plural = 'Виды грузов'
