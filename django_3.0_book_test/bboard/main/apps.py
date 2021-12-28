from django.apps import AppConfig
from django.dispatch import Signal
from .utilites import send_activation_notification


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


# код который объявит сигнал user _ registered и привяжет к нему обработчик стр 617
user_registered = Signal(providing_args=['instance'])


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatcher)
