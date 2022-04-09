from django.apps import AppConfig
from django.dispatch import Signal
from .utilities import send_activation_notification


class BulletinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bulletin_board'


# объявит сигнал user _ registered и привяжет к нему обработчик
user_registered = Signal(providing_args=['instance'])


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatcher)