from django.contrib import admin
from .models import *


admin.site.register(Book)
admin.site.register(PageLink)
admin.site.register(Item)

admin.site.register(Note)
admin.site.register(DroppedItem)

admin.site.register(ProgressConditionItem)


class BookPageAdmin(admin.ModelAdmin):
    filter_horizontal = ('page_items',)


class BookProgressAdmin(admin.ModelAdmin):
    filter_horizontal = ('inventory_items',)


class AdminProgressCondition(admin.ModelAdmin):
    filter_horizontal = ('items',)


admin.site.register(BookPage, BookPageAdmin)
admin.site.register(BookProgress, BookProgressAdmin)
admin.site.register(ProgressCondition, AdminProgressCondition)


