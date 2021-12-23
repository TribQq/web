from django.db import models

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

    class Meta:
        verbose_name_plural = 'Ad'
        verbose_name = 'Ads'
        ordering = ['-published'] #сортируем обьекты по дате публикации(- отввечает за реверсивную сортировку)
