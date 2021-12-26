from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser): #грейдим встроенную модель юзера
    is_activated = models.BooleanField(default=True,db_index=True,verbose_name='Активация пройдена')

    send_messages = models.BooleanField(default=True,verbose_name='Отправлять ли оповещения?')

    class Meta:
        pass
