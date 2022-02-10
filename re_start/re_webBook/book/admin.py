from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(BookPage)
admin.site.register(PageLink)
admin.site.register(Item)
admin.site.register(BookProgress)