from django.db import models
from django.contrib.auth.models import AbstractUser


# шаблогы для бд(нужн а миграция)


class AdvUser(AbstractUser):  # грейдим встроенную модель юзера
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активация пройдена')
    send_messages = models.BooleanField(default=True, verbose_name='Отправлять ли оповещения?')

    class Meta:
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
        return super().get_queryset().filter(super_rubric__isnull=False) # Диспетчер записей SuЬRuЬricManager будет отбирать лишь
        # записи с непустым полем super_ruЬric (т. е. подрубрики)

class SubRubric(Rubric):
    object = SubRubricManager()

    def __str__(self):
        return '%s - %s' % (self.super_rubric.name,self.name)

    class Meta:
        proxy = True
        ordering = ('super_rubric__order', 'super_rubric__name', 'order', 'name')
        verbose_name = 'Подрубрика'
        verbose_name_plural = 'Подрубрики'