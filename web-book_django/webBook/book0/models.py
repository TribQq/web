from django.db import models


# Create your models here.


class Book(models.Model):
    """interactive function ."""
    title = models.TextField(name='title', unique=True)

    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self) # Возвращаем имя для админки (и вообще)1:46/0



class BookPage(models.Model):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE)  # ForeginKey - нативная ссылка для базы(1:33)0ур # foreginkey-всегда отношение многие к одному(многие стр к одной книге)
    title = models.TextField(name='title')
    body = models.TextField(name='body')
    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)


class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage, related_name='frommaterial', on_delete=models.CASCADE)  # ForeginKey - нативная ссылка для базы(1:33)0ур # foreginkey-всегда отношение многие к одному(многие стр к одной книге)
    to_page = models.ForeignKey(BookPage, related_name='tomaterial', on_delete=models.CASCADE) # нужно было перереиминовать related_name чтоб он его не подтягивал из бука 2'02||0
    name = models.TextField()
    def __str__(self):
        return ('{self.from_page.title} --> {self.to_page.title} '\
               '({self.id})'.format(
                    self=self,
                    )
                )
    class Meta:
        unique_together = ['from_page', 'to_page'] # уникальность + многие ко многим 2:01
