from django.contrib import admin
from .models import *

admin.site.register(Rubric)

class BbAdmin(admin.ModelAdmin):
    list_display = ('title','content','price','published','rubric') #вывод полей
    list_display_links = ('title','content') #проеборазование в гиперссылки
    search_fields = ('title', 'content') #фильтрация по

admin.site.register(Bb,BbAdmin)


# Register your models here.
