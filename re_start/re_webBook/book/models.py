from django.db import models
from django.contrib.auth.models import User


from .utilities import get_timestamp_path


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    first_page = models.OneToOneField('BookPage', blank=True, null=True, related_name='first_page', verbose_name='Стартовая страница', on_delete=models.SET_NULL)
    cover_img = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Обложка книги')


class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    text = models.TextField()
    page_items = models.ManyToManyField('Item', blank=True)

    def __str__(self):
        return self.title


class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    to_page = models.ForeignKey(BookPage, related_name='to_page', on_delete=models.CASCADE)
    name_path = models.CharField(null=True, blank=True, max_length=50)
    key_items = models.ManyToManyField('Item', blank=True)

    def __str__(self):
        return ('{self.from_page.title} --> {self.to_page.title} ' \
                '({self.id})'.format(
            self=self,
        )
        )

    class Meta:
        unique_together = ['from_page', 'to_page']

    def check_key_items(self, inventory_items: list) -> bool:
        check_result: bool = all(key in inventory_items for key in self.key_items.all())
        return check_result





class BookProgress(models.Model): # трабла в автосоздании новой модельки под новою книгу+юзера (т.е если ручками создать поле в бд то ок инече краш)
    """idk"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    inventory_items = models.ManyToManyField('Item', blank=True)

    class Meta:
        unique_together = ['user', 'book']

    @classmethod
    def start_progress(cls, user, book):
        page = book.first_page if book.first_page else BookPage.objects.filter(book_id=book.id)[0] #если страницы по умолчанию нет, то ,берём страницу с меньшим id у этой книжки
        progress = BookProgress(user=user, book=book, book_page=page)
        progress.save()
        return progress

    def save_to(self, save_id):
        if save_id is None:
            state = ProgressSave.objects.create(progress=self,
                                                book_page=self.book_page)
            state.inventory.set(self.inventory_items.all()) # ? но по другому кряк, указвывет можноство итемов в porgressSave через множество итемов в progresse`e
        else:
            state = ProgressSave.get(id=save_id)
            state.update(progress=self, book_page=self.book_page,
                         inventory=self.inventory_items.all()) # upd т.к мы обновляем бд #_set Quertyset

    def save_load(self, save_id):
        state = ProgressSave.objects.get(id=save_id)
        self.update(book_page=state.book_page,
                    inventory_items=state.inventory)


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProgressSave(models.Model): # generate migration
    progress = models.ForeignKey(BookProgress, on_delete=models.CASCADE)
    save_time = models.DateTimeField(auto_now=True)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    inventory = models.ManyToManyField(Item, blank=True)