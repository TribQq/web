from django.db import models
from django.contrib.auth.models import AbstractUser

#шаблогы для бд(нужн а миграция)


class AdvUser(AbstractUser): #грейдим встроенную модель юзера
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активация пройдена')
    send_messages = models.BooleanField(default=True, verbose_name='Отправлять ли оповещения?')
    # test_text = models.TextField(verbose_name='Тестовый текст внутри')
    class Meta:
        pass
