from django.contrib.auth.models import User
from django.db import models

from .utilities import *

from easy_thumbnails.fields import ThumbnailerImageField


# Create your models here.


class Book(models.Model):
    """interactive function ."""
    title = models.TextField(name='title', unique=True, verbose_name='Название')
    cover_img = models.ImageField(upload_to=get_timestamp_path, blank=True, null=True, verbose_name='Изборажение')
    first_page = models.OneToOneField('BookPage', related_name='first_page', blank=True, null=True,
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
    title = models.CharField(name='title', max_length=70)
    body = models.TextField(name='body')
    items = models.ManyToManyField('Item', blank=True)

    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)


class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage,
                                  on_delete=models.CASCADE)  # ForeginKey - нативная ссылка для базы(1:33)0ур # foreginkey-всегда отношение многие к одному(многие стр к одной книге)
    to_page = models.ForeignKey(BookPage, related_name='to_page',
                                on_delete=models.CASCADE)  # нужно было перереиминовать related_name чтоб он его не подтягивал из бука 2'02||0
    name = models.TextField()
    items = models.ManyToManyField('book0.Item', blank=True)  # итемы необходимы для прохода

    # проблема была в 2 related_name, нужно было как то указать, или удалить родительский

    def __str__(self):
        return ('{self.from_page.title} --> {self.to_page.title} ' \
                '({self.id})'.format(
            self=self,
        )
        )

    def check_items(self, items):
        return all(i in items for i in
                   self.items.all())  # для i в pagelink.ttems.all() т.е каждый итем в списке условия мы проверяем на наличие в списке переданном в функц

    class Meta:
        unique_together = ['from_page', 'to_page']  # уникальность + многие ко многим 2:01


class BookProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE)  # каскадное удаление прогресса в и пр в случае удаления книги/юзера
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)

    items = models.ManyToManyField('book0.Item',
                                   blank=True)  # описание в джанго терминлогогии( book0 ==app(приложение) , Item ==model name)/поздняя динам запись 1:01(2)

    class Meta:
        unique_together = ('user', 'book')

    @classmethod
    def start_reading(cls, user, book):
        progress = BookProgress(user=user, book=book,
                                book_page=book.first_page)  # создаём прогресс в случае остуствия, + сэйв в бд + return в контроллер (# book=book.id == ошибка т.к нам нужен не айдишник а сам элемент бд)
        progress.save()
        return progress

    def save_to(self, save_id):
        if save_id is None:  # none t.k id can be 0
            state = ProgressSave.objects.create(progress=self, # create new obj bd in tabl progressave +(and) add in variable(переменная)
                                                book_page=self.book_page,
                                                )  # 1 44 (4)
            state.items.set(self.items.all()) # ?) множеству итемов этого сохраниния присваивается множество итемов прогресса (пачке присвоить пачку)
        else:
            state = ProgressSave.objects.get(id=save_id) # берём по id
            state.book_page = self.book_page # upd page
            state.items.set=self.items.all() # upd items .set нужно писать из множества и связи мэйни ту мэни
            state.save()

    def load_from(self, save_id):
        state = ProgressSave.objects.get(id=save_id) # get obj from bd
        self.book_page=state.book_page # upd progress # .update у себя не роб ит
        self.save()
        self.items.set(state.items.all())


class Item(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class ProgressSave(models.Model):
    progress = models.ForeignKey(BookProgress,
                                 on_delete=models.CASCADE)  # один элемент и табл bookprogress в бд может быть привязан ко множеству сейвов
    updated_at = models.DateTimeField(
        auto_now=True)  # auto_now - обновляет метку каждый раз при изменении в стр бд; auto_now_add- только при создании строки в бд
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)  # зачем , если это уже в прогрессе?
    items = models.ManyToManyField('book0.Item', blank=True)
