from django.db import models
from django.db.models import SET_NULL,CASCADE
from django.contrib.auth.models import User


from .utilities import get_timestamp_path

class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    first_page = models.OneToOneField('BookPage', blank=True, null=True, related_name='first_page', verbose_name='Стартовая страница', on_delete=SET_NULL)
    cover_img = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Обложка книги')


class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=CASCADE)
    title = models.TextField(blank=True, null=True)
    text = models.TextField()
    item = models.ForeignKey('Items', blank=True, null=True, on_delete=SET_NULL)
    def __str__(self):
        return self.title


class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage, on_delete=CASCADE)
    to_page = models.ForeignKey(BookPage, related_name='to_page', on_delete=CASCADE)
    name_path = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        if self.name_path != None:
            return self.name_path
        return '%s --> %s' % (self.from_page.title, self.to_page.title)

    class Meta:
        unique_together = ['from_page', 'to_page']


class BookProgress(models.Model):
    """idk"""
    user = models.ForeignKey(User, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)
    page = models.ForeignKey(BookPage, on_delete=CASCADE)

    @classmethod
    def start_progress(cls):
        """pass"""
        progress_page = ''
        return progress_page

    class Meta:
        unique_together = ['user', 'book']


class Items(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()