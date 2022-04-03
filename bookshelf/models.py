from typing import Tuple
from django.db import models, transaction
from bulletin_board.models import AdvUser as User

from .utilities import get_timestamp_path


class Test(models.Model):
    bool_null = models.BooleanField(default=None, null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=10, default='Book', verbose_name='Title')
    subtitle = models.CharField(max_length=15, default='Name', verbose_name='Subtitle')
    desc_title = models.CharField(max_length=10, null=True, blank=True, verbose_name='Title description')
    desc_subtitle = models.CharField(max_length=15, null=True, blank=True, verbose_name='Subtitle description')
    desc_text = models.TextField(max_length=300, default='Lorem ispum description', verbose_name='Description')
    first_page = models.OneToOneField('BookPage', blank=True, null=True, related_name='first_page', verbose_name='Start stage', on_delete=models.SET_NULL)
    cover_img = models.ImageField(blank=True, null=True,
                                  upload_to=get_timestamp_path, verbose_name='Image on book cover')

    inventory_limit = models.IntegerField(default=10)
    progress_conditions = models.ManyToManyField('ProgressCondition', verbose_name='lose/win conditions', blank=True)

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'


class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True,
                              upload_to=get_timestamp_path, verbose_name='Page image')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    inventory_items = models.ManyToManyField('Item', blank=True)
    end_status = models.BooleanField(null=True, blank=True)
    # inventory_full = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'book']

    @classmethod
    def start_progress(cls, user, book):
        page = book.first_page if book.first_page else BookPage.objects.filter(book_id=book.id)[0] #если страницы по умолчанию нет, то ,берём страницу с меньшим id у этой книжки
        progress = BookProgress(user=user, book=book, book_page=page)
        progress.save()
        return progress

    def check_items_position(self, checked_i, inventory_i, dropped_i_p) -> list[bool, ...]:
        item_on_position: list[bool, ...] = []
        for i in checked_i:
            if i['page_position'] is None:
                item_on_position.append((i['item'] in inventory_i))
            elif i['page_position'] in dropped_i_p.keys():
                item_on_position.append(i['item'] in dropped_i_p[i['page_position']])
            else:
                item_on_position.append(False)
        return item_on_position

    def try_end_progress(self, book_id: int) -> any:
        """collect all win/lose conditions =>  check status if something true => return w_page"""
        progress_conditions = Book.objects.get(id=book_id).progress_conditions.all()
        for condition in progress_conditions:
            condition_items: list[dict[str, str], ...] = list(condition.status_items.all().values('item', 'page_position'))
            inventory_items: list[str, ...] = list(self.inventory_items.all().values_list('id', flat=True))
            dropped_items_pages: dict[int, list[int, ...]] = {}

            for di in self.droppeditem_set.all().values('item', 'book_page_id'):
                try:
                    dropped_items_pages[di['book_page_id']].append(di['item'])
                except:
                    dropped_items_pages[di['book_page_id']] = [di['item']]

            # не раб на нескольких условиях
            item_on_position: list[bool, ...] = self.check_items_position(condition_items, inventory_items, dropped_items_pages)
            print(item_on_position)
            if False not in item_on_position:
                return condition.final_page
        return False

    def end_progress(self, final_page):
        self.book_page = final_page
        self.end_status = True
        self.save()

    @transaction.atomic
    def save_to(self, save_id):
        if save_id is None:
            state = ProgressSave.objects.create(
                progress=self, book_page=self.book_page)
        else:
            state = ProgressSave.objects.get(id=save_id)
            state.progress = self
            state.book_page = self.book_page
            state.droppeditemsave.all().delete()
        state.inventory_items.set(self.inventory_items.all())
        for di in self.droppeditem_set.all():
            DroppedItemSave.objects.create(item=di.item, book_page=di.book_page,
                                            progress_save=state)
        state.save()

    @transaction.atomic
    def save_load(self, save_id):
        state = ProgressSave.objects.get(id=save_id)
        self.book_page = state.book_page
        self.inventory_items.set(state.inventory_items.all())
        self.droppeditem_set.all().delete()
        for dis in state.droppeditemsave_set.all():
            DroppedItem.objects.create(item=dis.item, book_page=dis.book_page,
                        progress=state.progress)
        self.save()


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DroppedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    progress = models.ForeignKey(BookProgress, on_delete=models.CASCADE)

    def __str__(self):
        return '{self.item.name} ({self.book_page.title})'.format(self=self)


class ProgressSave(models.Model):
    progress = models.ForeignKey(BookProgress, on_delete=models.CASCADE)
    save_time = models.DateTimeField(auto_now=True)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    inventory_items = models.ManyToManyField(Item, blank=True)


class DroppedItemSave(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    progress_save = models.ForeignKey(ProgressSave, on_delete=models.CASCADE)


class Note(models.Model):
    title = models.TextField(max_length=10)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE, blank=True, null=True)
    pinned = models.BooleanField(default=False)


class ProgressConditionStatusItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE) # , related_name='customItem'
    desc = models.CharField(default='description', verbose_name='description', max_length=60)
    page_position = models.ForeignKey(BookPage, null=True, blank=True, on_delete=models.SET_NULL) # if none => inventory pos

    def __str__(self):
        return f'{self.item.name},{self.page_position}' #


class ProgressCondition(models.Model):
    status_items = models.ManyToManyField(ProgressConditionStatusItem)
    final_page = models.ForeignKey(BookPage, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(default='#noname', max_length=25)
    win_status = models.BooleanField(blank=True, null=True) # False-lose, True-win не нужно т.к заглушка энивей будет текстом(хотя для доп функций можоно будет доабвить)

    def __str__(self):
        return f'condotion:({self.id}): items({[pi.item.name for pi in self.status_items.all()]}'


