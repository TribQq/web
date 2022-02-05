from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(BookPage)
admin.site.register(PageLink)

# admin.site.register(Bb)

class AdditionalImageInline(admin.TabularInline):
    model = BookAdditionalImage


class BookAdmin(admin.ModelAdmin):
    list_display = ('title')


# admin.site.register(Book, BookAdmin)
