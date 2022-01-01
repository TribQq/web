#gghhggdass55Z User0-User1 passwords

from django.contrib import admin
import datetime


from .models import AdvUser
from .utilities import send_activation_notification


# admin.site.register(AdvUser) # рега модели юзера (стр603) #делит стр 623


def send_activation_notifications(modeladmin, request, queryset):  # стр 623
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письмо для активации было отправлено')


send_activation_notifications.short_description = 'Отправка письма активации'


class NonacitvatedFilter(admin.SimpleListFilter):  # стр 624
    # я выполнения фильтрации пользователей, выполнивших активацию, не выполнивших ее в течение
    title = 'Статус активации:'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Прошли'),
            ('threedays', 'Не прошли более 3х дней'),
            ('week', 'Не прошли более недели'),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonacitvatedFilter,)

    fields = (('username', 'email'),
              ('first_name', 'last_name'),
              ('password'),
              ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    # Мы явно указываем список полей, которые должны выводиться в формах для правки пользователей, чтобы выстроить их в удобном для работы порядке
    readonly_fields = ('last_login', 'date_joined')  # делаем доступными только для чтения.
    actions = (
    send_activation_notifications,)  # ц, регистрируем действие, которое разошлет пользователям письма с предписаниями выполнить активацию.
    # Это действие реализовано функцией send_activation _ notifications (). В ней мы перебираем всех выбранных пользователей
    # и для каждого, кто не выполнил активацию, вызываем функцию send_activation_notification (),
    # объявленную ранее в модуле uti lities.py и непосредственно производящую отправку писем.


admin.site.register(AdvUser, AdvUserAdmin)
