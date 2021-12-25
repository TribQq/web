from django.contrib import admin
from .models import *

admin.site.register(Rubric) # регистрация модели Rubric(дефолт для всех моделей)

class BbAdmin(admin.ModelAdmin):
    list_display = ('title','content','price','published','rubric') # вывод полей
    list_display_links = ('title','content') # делает контент этих полей ссылками
    search_fields = ('title', 'content') # можно сёрчить по этим полям в админке

admin.site.register(Bb,BbAdmin)


# Register your models here.
