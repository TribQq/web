from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


# Модель - это класс, описывающий одну из таблиц в БД и инструменты для работы с ней стр86

class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE) # OneToOneField == 1-1 отношение , CASCADE== каскадное удаление(всё связанное с юзером)
    # связываем импортед юзера с данной моделью 1-1 связью (99стр)


class Spare(models.Model):
    name = models.CharField(max_length=30)

class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyТoManyField(Spare)
    #связывает машины и детали типом многие ко многим (стр 100)


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']

class Bb(models.Model):
    # создание модели(подкласс класса Model из модуля django.db.models)
    # артрибуты класса с различными экземплярами класса
    title = models.CharField(max_length=50,verbose_name= 'product')
    content = models.TextField(null=True, blank=True,verbose_name= 'description') #null и blank конструктора значения True= полеможно не заполнять (по умолчанию любое поле обязательно к заполнению)
    price = models.FloatField(null=True, blank=True,verbose_name= 'price') #null и blank конструктора значения True= полеможно не заполнять (по умолчанию любое поле обязательно к заполнению)
    published = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name= 'published')

    rubric = models.ForeignKey('Rubric', null=True , on_delete=models.PROTECT,verbose_name='Rubric')
    # установка связи 1-многие где рубрика==1 модели== многие стр 54
    # и 96(разное оформление при разной позиции первычного класса к вторичному) и пр детали доки

    class Kinds(models.TextChoices):
        # Перечисление должно являться подклассом класса тextChoices стр 95
        BUY = 1, ' Куплю'
        SELL = 2, ' Продам '
        EXCНANGE = 3, ' Обменяю'
        RENT = 4
        __empty__ = 'Выберите ти публикуемого обьявления' # задаёт внешнее определения для полей у которых не указанно внешний тип( 2 й пункт )
    # список(tupl в данном случае с кортежами внутри) значений списка которые будт использованны далее
    kind = models.CharField(max_length=1, choices=Kinds.choices,
                            default=Kinds.SELL)


    class Meta:
        verbose_name_plural = 'Ad'
        verbose_name = 'Ads'
        ordering = ['-published'] #сортируем обьекты по дате публикации(- отввечает за реверсивную сортировку)

    def clean(self):
        #ввод обязательных полей для заполнен и чек на отриц прайс (стр 117)
        # но её ведь ничего не вызывает?
        errors = {}
        if not self.content:
            errors[' content '] = ValidationError(' Yкaжитe описание ' +' продаваемого товара ')
        if self.price and self.price < 0:
            errors[' price ']
        if errors:
            ValidationError(' Yкaжитe ' + ' неотрицательное значение цены ')
        raise ValidationError(errors)
