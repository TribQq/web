from django.db import models
from django.db.models import SET_NULL,CASCADE


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    first_page = models.OneToOneField('BookPage', blank=True, null=True, related_name='first_page', verbose_name='Стартовая страница', on_delete=SET_NULL)


class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=CASCADE)
    title = models.TextField(blank=True, null=True)
    text = models.TextField()


class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage, on_delete=CASCADE)
    to_page = models.ForeignKey(BookPage, related_name='to_page', on_delete=CASCADE)

    def __str__(self):
        return ('{self.from_page.title} --> {self.to_page.title} '
                '({self.id})'.format(self=self, )
                )

    class Meta:
        """idk"""
        unique_together = ['from_page', 'to_page']
