from django.db import models

from .utilities import *


# Create your models here.


class Book(models.Model):
    """interactive function ."""
    title = models.TextField(name='title', unique=True , verbose_name='Название')
    cover_img = models.ImageField(upload_to=get_timestamp_path, null=True, verbose_name='Изборажение')

    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self) # Возвращаем имя для админки (и вообще)1:46/0

    def delete(self, *args, **kwargs ):
        for ai in self.BookadditionalImage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'


class BookAdditionalImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Обложка')

    class Meta:
        verbose_name_plural = 'Доп иллюстрации'
        verbose_name = 'Доп иллюстрация'


class BookPage(models.Model):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE)  # ForeginKey - нативная ссылка для базы(1:33)0ур # foreginkey-всегда отношение многие к одному(многие стр к одной книге)
    title = models.TextField(name='title')
    body = models.TextField(name='body')

    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)


class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)  # ForeginKey - нативная ссылка для базы(1:33)0ур # foreginkey-всегда отношение многие к одному(многие стр к одной книге)
    to_page = models.ForeignKey(BookPage, related_name='to_page', on_delete=models.CASCADE) # нужно было перереиминовать related_name чтоб он его не подтягивал из бука 2'02||0
    name = models.TextField()
    # проблема была в 2 related_name, нужно было как то указать, или удалить родительский
    def __str__(self):
        return ('{self.from_page.title} --> {self.to_page.title} '\
               '({self.id})'.format(
                    self=self,
                    )
                )
    class Meta:
        unique_together = ['from_page', 'to_page'] # уникальность + многие ко многим 2:01



class Bb(models.Model):
    title = models.CharField(max_length=40, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    contacts = models.TextField(max_length=80, verbose_name='Контакты')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить в списке?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():  # перед удалением текущей записи мы перебираем
            ai.delete()  # и вызовом метода delete () удаляем все связанные дополнительные иллюстрации.
        super().delete(*args,
                       **kwargs)  # При вызове метода delete () возникает сигнал post _ delete, обрабатываемый приложением dj ango _ cleanup
        # , которое в ответ удалит все файлы, хранящиесяв удаленной записи.

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-created_at']


class AdditionalImage(models.Model): # модель доп иллюстраций
    bb = models.ForeignKey(Bb, on_delete=models.CASCADE, verbose_name='Обьявление')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Доп иллюстрации'
        verbose_name = 'Доп иллюстрация'