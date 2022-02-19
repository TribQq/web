from django.contrib import admin
from .models import *


admin.site.register(Item)
admin.site.register(DroppedItem)
admin.site.register(ProgressSave)


class AdditionalImageInline(admin.TabularInline):
    model = BookAdditionalImage


class BookAdmin(admin.ModelAdmin):
    change_form_template = 'admin/book_change_form.html'


class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('items', )


admin.site.register(Book, BookAdmin)
admin.site.register(BookPage, ItemAdmin)
admin.site.register(PageLink, ItemAdmin)

admin.site.register(BookProgress, ItemAdmin)
