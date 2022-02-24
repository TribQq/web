from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(PageLink)
admin.site.register(Item)
admin.site.register(WinCondition)
admin.site.register(LoseCondition)

class BookPageAdmin(admin.ModelAdmin):
    filter_horizontal = ('page_items',)


admin.site.register(BookPage, BookPageAdmin)


class BookProgressAdmin(admin.ModelAdmin):
    filter_horizontal = ('inventory_items',)


admin.site.register(BookProgress , BookProgressAdmin)

