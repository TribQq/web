from django.db import models
from django.contrib.auth.models import AbstractUser

from .utilities import get_timestamp_path


# шаблогы для бд(нужн а миграция)


class AdvUser(AbstractUser):  # грейдим встроенную модель юзера
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активация пройдена')
    send_messages = models.BooleanField(default=True, verbose_name='Отправлять ли оповещения?')

    def delete(self, *args,
               **kwargs):  # сделаем так, чтобы при удалении пользователя удалялись оставленные им объявления:
        for bb in self.bb_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        pass


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True,
                                     verbose_name='Порядок')  # целое число, обозначающее порядок следования рубрик
    super_rubric = models.ForeignKey('SuperRubric', on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Надрубрика')  # е super_ruЬric будет хранить надрубрику, к которой относится текущая подрубрика
    # Оно будет иметь следующие важные особенности: связь, создаваемая этим полем, должна устанавливаться с моделью надрубрик
    # это поле будет заполняться только в том случае, если запись хранит подрубрику
    #  нужно обязательно запретить каскадное удаление записей


# Чтобы изменить состав обрабатываемых моделью записей, нужно задать для нее свой диспетчер записей, который и укажет необходимые условия фильтрации
class SuperRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=True)


# Для работы с надрубриками объявим прокси-модель superRuЬric, производную от RuЬric
# (прокси-модель позволяет менять лишь функциональность модели, но не набор объявленных в ней полей,
# однако нам и надо изменить лишь функциональность модели  Она будет обрабатывать только надрубрики.
class SuperRubric(Rubric):
    objects = SuperRubricManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order', 'name')
        verbose_name = 'Надрубрика'
        verbose_name_plural = 'Надрубрики'


class SubRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            super_rubric__isnull=False)  # Диспетчер записей SuЬRuЬricManager будет отбирать лишь
        # записи с непустым полем super_ruЬric (т. е. подрубрики)


class SubRubric(Rubric):
    object = SubRubricManager()

    def __str__(self):
        return '%s - %s' % (self.super_rubric.name, self.name)

    class Meta:
        proxy = True
        ordering = ('super_rubric__order', 'super_rubric__name', 'order', 'name')
        verbose_name = 'Подрубрика'
        verbose_name_plural = 'Подрубрики'


class Bb(models.Model):
    rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=40, verbose_name='Товар')
    content = models.TextField(verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    contacts = models.TextField(max_length=80, verbose_name='Контакты')
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, verbose_name='Автор обьявления ')
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


class Comment(models.Model):
    bb = models.ForeignKey(Bb, on_delete=models.CASCADE, verbose_name='Обьявление')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-created_at']
