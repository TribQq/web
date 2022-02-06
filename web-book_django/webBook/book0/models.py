from django.contrib.auth.models import User
from django.db import models

from .utilities import *

from easy_thumbnails.fields import ThumbnailerImageField


# Create your models here.


class Book(models.Model):
    """interactive function ."""
    title = models.TextField(name='title', unique=True, verbose_name='Название')
    cover_img = models.ImageField(upload_to=get_timestamp_path, null=True, verbose_name='Изборажение')
    first_page = models.OneToOneField('BookPage', related_name='first_page', null=True,
                                      on_delete=models.SET_NULL)  # кавычки т.к моделька ниже , + related_name нужно т.к перекрётсное отношение моделек ,on_delete, в случает удаления обьекта устанвливается значение нул

    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)  # Возвращаем имя для админки (и вообще)1:46/0

    def delete(self, *args, **kwargs):
        for ai in self.BookadditionalImage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'


class BookAdditionalImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    cover_img = models.ImageField(upload_to=get_timestamp_path, verbose_name='Обложка')

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
    from_page = models.ForeignKey(BookPage,
                                  on_delete=models.CASCADE)  # ForeginKey - нативная ссылка для базы(1:33)0ур # foreginkey-всегда отношение многие к одному(многие стр к одной книге)
    to_page = models.ForeignKey(BookPage, related_name='to_page',
                                on_delete=models.CASCADE)  # нужно было перереиминовать related_name чтоб он его не подтягивал из бука 2'02||0
    name = models.TextField()

    # проблема была в 2 related_name, нужно было как то указать, или удалить родительский
    def __str__(self):
        return ('{self.from_page.title} --> {self.to_page.title} ' \
                '({self.id})'.format(
            self=self,
        )
        )

    class Meta:
        unique_together = ['from_page', 'to_page']  # уникальность + многие ко многим 2:01


class BookProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # каскадное удаление прогресса в и пр в случае удаления книги/юзера
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)

    items = models.ManyToManyField('book0.Item') # описание в джанго терминлогогии( book0 ==app(приложение) , Item ==model name)/поздняя динам запись 1:01(2)

    class Meta:
        unique_together = ('user', 'book')

    @classmethod
    def start_reading(cls, user, book):
        progress = BookProgress(user=user, book=book, book_page=book.first_page) # создаём прогресс в случае остуствия, + сэйв в бд + return в контроллер
        progress.save()
        return progress


class Item(models.Model):
    name = models.TextField()
