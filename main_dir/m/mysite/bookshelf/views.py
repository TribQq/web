from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from bulletin_board.models import AdvUser as User
from .models import *
from .forms import *


def view_plug(request):
    return HttpResponse('just plug')


def view_onlyScroll(request):
    return render(request, 'layout/scroll_basic.html')



def _return_to_main(book_id):
    return redirect(reverse('read_book', kwargs={'book_id': book_id}))


def _return_to_main_anchor(book_id:int, anchor:str):
    return redirect(reverse('read_book_anchor', kwargs={'book_id': book_id})+ anchor)



def on_progress(view):
    def inner(request, book_id, **kwargs):
        book = get_object_or_404(Book, id=book_id) # мы НЕ хотим 2 раза идти в бд...
        try:
            progress = BookProgress.objects.get(book=book, user=request.user)
        except BookProgress.DoesNotExist:
            return redirect(reverse('book_main', kwargs={'book_id': book_id}))
        return view(request=request, progress=progress, book_id=book_id, **kwargs)
    return inner


def view_bookshelf(request):
    max_book = 11
    books = Book.objects.all()[:max_book]
    context = {'books': books, }
    return render(request, 'bookshelf.html', context=context)


def get_read_book_context(progress, book) : #-> dict[any,any, ...]
    page = progress.book_page
    links: list[tuple[any, bool], ...] = [
        (link, link.check_key_items(progress.inventory_items.all()))
        for link in page.pagelink_set.all()
    ]
    location_items = page.page_items.exclude(
        id__in=progress.inventory_items.all().values_list('id', flat=True)).exclude(
        id__in=progress.droppeditem_set.filter(progress=progress).values_list('item__id', flat=True))
    dropped_items = DroppedItem.objects.filter(book_page=page.id)
    pinned_notes = book.note_set.filter(pinned=True)
    page_notes = book.note_set.filter(pinned=False, book_page=page)
    notes = book.note_set.exclude(
        id__in=[n.id for n in pinned_notes]).exclude(id__in=[n.id for n in page_notes])
    context = {'book': book, 'page': page,
               'link_status_tuple': links, 'progress': progress,
               'location_items': location_items, 'dropped_items': dropped_items,
               'pinned_notes': pinned_notes, 'notes': notes, 'page_notes': page_notes,
               'NoteFrom': NoteForm,
               }
    return context

def view_read_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        progress = BookProgress.objects.get(book=book, user=request.user)
    except BookProgress.DoesNotExist:
        progress = BookProgress.start_progress(user=request.user, book=book)   
    context = get_read_book_context(progress, book)

    return render(request, 'book_page.html', context)


@on_progress
def go_to(request,progress, book_id, link_id): #реализовать привязку к линку т.к ?)
    page_link = get_object_or_404(PageLink, id=link_id)
    if (
        progress.book_page.id == page_link.from_page.id
        and
        page_link.check_key_items(progress.inventory_items.all())
    ):
        progress.book_page = page_link.to_page
        progress.save()
    context = {'book_id': book_id}
    return redirect(reverse('view_read_book', kwargs=context))


@on_progress
def view_saves(request, progress, book_id):
    """save page"""
    context = {'book': Book.objects.get(id=book_id),
               'progress': progress,
               'saves': progress.progresssave_set.all()}
    return render(request, 'save_page.html', context)


@on_progress
def view_save_to(request, progress, book_id, save_id=None):
    """new/upd save"""
    save = progress.save_to(save_id=save_id)
    # upd/ save ?
    context = {'book_id': book_id, }
    return redirect(reverse('saves', kwargs=context))



@on_progress
def view_load_from(request, progress, book_id, save_id):
    progress.save_load(save_id)
    context = {'book_id': book_id}
    return redirect(reverse('saves', kwargs=context))


@on_progress
def view_delete_save(request, progress, book_id, save_id):
    save = get_object_or_404(ProgressSave, id=save_id)
    save.delete()
    return redirect(reverse('saves', kwargs={'book_id': book_id}))



@on_progress
def take_item(request, progress, book_id, item_id):
    item = get_object_or_404(Item, id=item_id)
    progress.inventory_items.add(item)
    context = {'book_id': book_id}
    return redirect(reverse('view_read_book', kwargs=context))


@on_progress
def drop_item(request, progress, book_id, item_id):
    item = get_object_or_404(Item, id=item_id)
    progress.inventory_items.remove(item)
    progress.save()
    DroppedItem.objects.create(
        item=item,
        book_page=progress.book_page,
        progress=progress,
        book=progress.book
    )
    return _return_to_main(book_id)

@on_progress
def take_back_item(request, progress, book_id, item_id): # TODO  need transaction btw
    dropped_item = get_object_or_404(DroppedItem, id=item_id)
    progress.inventory_items.add(dropped_item.item)
    dropped_item.delete()
    return redirect(reverse('book_main', kwargs={'book_id': book_id}))




def view_add_note(request, book_id):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        Note.objects.create(
            title=request.POST['title'],

            text=request.POST['text'],
            book=Book.objects.get(id=book_id)
        )
    anchor = '#notes_block'
    return _return_to_main_anchor(book_id=book_id, anchor=anchor)

def view_delete_note(request, book_id, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    anchor = '#notes_block'
    return _return_to_main_anchor(book_id=book_id, anchor=anchor)


def view_toggle_pin(request, book_id, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.pinned = True if note.pinned == False else False
    note.save()
    anchor = '#notes_block'
    return _return_to_main_anchor(book_id=book_id, anchor=anchor)


@on_progress
def view_update_note(request, progress, book_id, note_id):
    selected_note = get_object_or_404(Note, id=note_id)
    print(request.method, '== request.method')
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        context = get_read_book_context(progress, book)
        context['selected_note'] = selected_note
        # context['change_note_form'] = ChangeNoteForm(request.POST, instance=selected_note) # для обновления формы(не использовал,а вписал в template ручками для разнообразия)
        return render(request,  'book_page.html', context=context)
    elif request.method == 'POST':
        print(request.POST, ' ==post')
        selected_note.title=request.POST['title']
        selected_note.text=request.POST['text']
        selected_note.book_page = None if request.POST['book_page'] == 'remove' else get_object_or_404(BookPage, id=request.POST['book_page']) # if upd by form.classs
        selected_note.pinned = True if 'pinned' in request.POST.keys() else False
        selected_note.save()

    return _return_to_main(book_id)





