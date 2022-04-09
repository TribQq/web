from django.contrib import admin
import datetime

from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .forms import SubRubricForm, AdvUserChangeForm
from .models import AdvUser, SuperRubric, SubRubric, Bb, AdditionalImage, Comment
from .utilities import send_activation_notification


def send_activation_notifications(modeladmin, request, queryset):
    """ email activation status """
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Письмо для активации было отправлено')


send_activation_notifications.short_description = 'Отправка письма активации'


class NonacitvatedFilter(admin.SimpleListFilter):
    """ filter for acc by non activate date and activate status """
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


class AdvUserAdmin(UserAdmin):
    """ user model fro admin """
    add_form = UserCreationForm
    form = AdvUserChangeForm
    model = AdvUser
    list_display = ['__str__', 'email', 'is_activated', 'date_joined', ] # first elem = link to change
    list_filter = (NonacitvatedFilter,)
    fieldsets = (
        ('section_0', {
            'fields': (('username', 'email'),
                       ('first_name', 'last_name'),
                       'password',
                       ('send_messages', 'is_active', 'is_activated'),
                       ('is_staff', 'is_superuser'),
                       'groups', 'user_permissions',
                       ('last_login', 'date_joined'))
        }),
    )

    readonly_fields = ('last_login', 'date_joined',)
    actions = (send_activation_notifications,)


admin.site.register(AdvUser, AdvUserAdmin)


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)


admin.site.register(SuperRubric, SuperRubricAdmin)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


admin.site.register(SubRubric, SubRubricAdmin)


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class CommentInBbAdmin(admin.StackedInline):
    model = Comment


class BbAdmin(admin.ModelAdmin):
    """ products with info for admin panel """
    list_display = ( 'title','rubric', 'content', 'author', 'created_at',)
    fields = (('rubric', 'author'), 'title', 'content', 'price', 'contacts', 'image', 'is_active',)
    inlines = (AdditionalImageInline, CommentInBbAdmin, )


admin.site.register(Bb, BbAdmin)


class CommentAdmin(admin.ModelAdmin):
    """ products comments for admin panel"""
    list_display = ('author', 'content', 'created_at', 'is_active')
    list_display_links = ('author', 'content')
    list_filter = ('is_active',)
    search_fields = ('author', 'content',)
    date_hierarchy = 'created_at'
    fields = ('author', 'content', 'is_active', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Comment, CommentAdmin)
