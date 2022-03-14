from django.db import models

from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated: bool = models.BooleanField(default=True, db_index=True, verbose_name='Account activated?')
    send_messages: bool = models.BooleanField(default=True, db_index=True, verbose_name='mailing enabled?')

    class Meta:
        """pass"""


