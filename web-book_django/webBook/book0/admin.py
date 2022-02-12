from django.contrib import admin
from .models import *


admin.site.register(Book)
# admin.site.register(BookPage)
# admin.site.register(PageLink)
admin.site.register(Item)

# admin.site.register(BookProgress)


class AdditionalImageInline(admin.TabularInline):
    model = BookAdditionalImage


class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ('items', )


admin.site.register(BookPage, ItemAdmin)
admin.site.register(PageLink, ItemAdmin)
admin.site.register(BookProgress, ItemAdmin)

# admin.site.register(Book, BookAdmin)
