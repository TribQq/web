from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title','slug', 'content', 'photo', 'get_html_photo', 'give_html_text', 'is_published', 'cat')
    readonly_fields = ('time_create','time_update','get_html_photo','give_html_text',) # если онли фото, то краш я хз поч

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')
    def give_html_text(self,object):
        if object.content:
            # return 'object.content' +' '+ mark_safe(f'<a href="https://www.google.com/">G</a>')
            return mark_safe(f'<p> random long text <a href="https://www.google.com/">Google_link</a></p>')

    get_html_photo.short_description = 'Миниатюра'
    get_html_photo.give_html_text = 'Миниатюра2'

    # def test_text(self):
    #     return mark_safe('test_text')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
