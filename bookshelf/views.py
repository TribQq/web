from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.db.models import QuerySet # for typehint

from bulletin_board.models import AdvUser as User
from .models import *
from .forms import *
# if  no auth. redirect to (create custom user)


def view_plug(request):
    return HttpResponse('just plug')


def view_onlyScroll(request) -> render:
    return render(request, 'layout/scroll_basic.html')


def _return_to_main(book_id: int) -> redirect:
    return redirect(reverse('bookshelf:view_read_book', kwargs={'book_id': book_id}))


def _return_to_main_anchor(book_id: int, anchor: str) -> redirect:
    return redirect(reverse('bookshelf:view_read_book', kwargs={'book_id': book_id}) + anchor)


def on_progress(view):
    """ work with progress create/update/check status"""
    def inner(request, book_id, **kwargs):
        book = get_object_or_404(Book, id=book_id) # мы НЕ хотим 2 раза идти в бд...
        try:
            progress = BookProgress.objects.get(book=book, user=request.user)
        except BookProgress.DoesNotExist:
            progress = BookProgress.start_progress(user=request.user, book=book)

        final_page = progress.try_end_progress(book_id=book_id)
        if final_page:
            progress.end_progress(final_page=final_page)

        return view(request=request, progress=progress, book_id=book_id, **kwargs)
    return inner


@on_progress
def view_drop_progress(request, progress, book_id: int) -> redirect:
    """ delete progress """
    progress.delete()
    return redirect(reverse('bookshelf:view_saves', kwargs={'book_id': book_id}))


def view_bookshelf(request) -> render:
    """ get some book => render page with this book queryset"""
    max_book = 11
    books = Book.objects.all()[:max_book]
    context = {'books': books, }
    return render(request, 'bookshelf.html', context=context)


def get_read_book_context(progress, book_id: int) -> dict[str, any]:
    """ context data for reading book """
    book = get_object_or_404(Book, id=book_id)
    page = progress.book_page
    links: list[tuple[any, bool], ...] = [
        (link, link.check_key_items(progress.inventory_items.all()))
        for link in page.pagelink_set.all()
    ]
    location_items: QuerySet = page.page_items.exclude(
        id__in=progress.inventory_items.all().values_list('id', flat=True)).exclude(
        id__in=progress.droppeditem_set.filter(progress=progress).values_list('item__id', flat=True))
    dropped_items: QuerySet = DroppedItem.objects.filter(book_page=page.id)
    pinned_notes: QuerySet = book.note_set.filter(pinned=True)
    page_notes: QuerySet = book.note_set.filter(pinned=False, book_page=page)
    notes = book.note_set.exclude(
        id__in=[n.id for n in pinned_notes]).exclude(id__in=[n.id for n in page_notes])
    win_conditions: QuerySet = book.progress_conditions.all().filter(win_status=True)
    inventory_full: bool = book.inventory_limit <= len(progress.inventory_items.all())
    context = {'book': book, 'page': page,
               'link_status_tuple': links, 'progress': progress,
               'location_items': location_items, 'dropped_items': dropped_items,
               'pinned_notes': pinned_notes, 'notes': notes, 'page_notes': page_notes,
               'NoteFrom': NoteForm, 'win_conditions': win_conditions,
               'inventory_full': inventory_full,
               }
    return context


@on_progress
def view_read_book(request, progress, book_id: int) -> render:
    """ main view for read book """
    context = get_read_book_context(progress=progress, book_id=book_id)
    return render(request, 'book_page.html', context)


@on_progress
def view_go_to(request, progress, book_id: int, link_id: int) -> redirect: #реализовать привязку к линку т.к ?)
    """ if page path validate for progress => update progress page """
    page_link = get_object_or_404(PageLink, id=link_id)
    if (
        progress.book_page.id == page_link.from_page.id
        and
        page_link.check_key_items(progress.inventory_items.all())
    ):
        progress.book_page = page_link.to_page
        progress.save()
    context = {'book_id': book_id}
    return redirect(reverse('bookshelf:view_read_book', kwargs=context))


@on_progress
def view_saves(request, progress, book_id: int) -> render:
    """ save page """
    context = {'book': Book.objects.get(id=book_id),
               'progress': progress,
               'saves': progress.progresssave_set.all()}
    return render(request, 'save_page.html', context)


@on_progress
def view_save_to(request, progress, book_id: int, save_id: int | None = None) -> redirect:
    """create/upd save"""
    save = progress.save_to(save_id=save_id)
    context = {'book_id': book_id, }
    return redirect(reverse('bookshelf:view_saves', kwargs=context))


@on_progress
def view_load_from(request, progress, book_id: int, save_id: int) -> redirect:
    """ update progress from save """
    progress.save_load(save_id)
    context = {'book_id': book_id}
    return redirect(reverse('bookshelf:view_saves', kwargs=context))


@on_progress
def view_delete_save(request, progress, book_id: int, save_id: int) -> redirect:
    """ delete save """
    save = get_object_or_404(ProgressSave, id=save_id)
    save.delete()
    return redirect(reverse('bookshelf:view_saves', kwargs={'book_id': book_id}))



@on_progress
def view_take_item(request, progress, book_id: int, item_id: int) -> redirect:
    """ upd progress, add item """
    item = get_object_or_404(Item, id=item_id)
    progress.inventory_items.add(item)
    context = {'book_id': book_id}
    return redirect(reverse('bookshelf:view_read_book', kwargs=context))


@on_progress
def view_drop_item(request, progress, book_id: int, item_id: int) -> redirect:
    """ upd dropped items model, add item + remove item from inventory"""
    item = get_object_or_404(Item, id=item_id)
    progress.inventory_items.remove(item)
    progress.save()
    DroppedItem.objects.create(
        item=item,
        book_page=progress.book_page,
        progress=progress,
    )
    return _return_to_main(book_id)


@on_progress
def view_take_back_item(request, progress, book_id: int, item_id: int) -> redirect: # TODO  need transaction btw
    """ remove item from dropped item model and add to progress """
    dropped_item = get_object_or_404(DroppedItem, id=item_id)
    progress.inventory_items.add(dropped_item.item)
    dropped_item.delete()
    return redirect(reverse('bookshelf:view_read_book', kwargs={'book_id': book_id}))


def view_add_note(request, book_id: int) -> redirect:
    """  create note """
    if request.method == 'POST':
        Note.objects.create(
            title=request.POST['title'],

            text=request.POST['text'],
            book=Book.objects.get(id=book_id)
        )
    anchor = '#notes_block'
    return _return_to_main_anchor(book_id=book_id, anchor=anchor)


def view_delete_note(request, book_id: int, note_id: int) -> redirect:
    """ delete note """
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    anchor = '#notes_block'
    return _return_to_main_anchor(book_id=book_id, anchor=anchor)


def view_toggle_pin(request, book_id: int, note_id: int) -> redirect:
    """ toggle note pin 'status' """
    note = get_object_or_404(Note, id=note_id)
    note.pinned = True if note.pinned == False else False
    note.save()
    anchor = '#notes_block'
    return _return_to_main_anchor(book_id=book_id, anchor=anchor)


@on_progress
def view_update_note(request, progress, book_id: int, note_id: int) -> redirect:
    """ update note """
    selected_note = get_object_or_404(Note, id=note_id)
    if request.method == 'GET':
        context = get_read_book_context(progress=progress, book_id=book_id)
        context['selected_note'] = selected_note
        # context['change_note_form'] = ChangeNoteForm(request.POST, instance=selected_note) # для обновления формы(не использовал,а вписал в template ручками для разнообразия)
        return render(request,  'book_page.html', context=context)
    elif request.method == 'POST':
        selected_note.title = request.POST['title']
        selected_note.text = request.POST['text']
        selected_note.book_page = None if request.POST['book_page'] == 'remove' else get_object_or_404(BookPage, id=request.POST['book_page']) # if upd by form.classs
        selected_note.pinned = True if 'pinned' in request.POST.keys() else False
        selected_note.save()
    anchor = '#notes_block'
    return _return_to_main_anchor(book_id=book_id, anchor=anchor)



