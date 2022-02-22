from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import *


def plug(request):
    return HttpResponse('just plug')


def _return_to(request, book_id):
    return redirect(reverse('book_main', kwargs={'book_id':book_id}))


def books_shelf(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/book_shelf.html', context)


# @on_progress
def book_titlePage(request, progress, book_id): # перенаправлять на фёрст мб + чек/создание прогресса
    b = get_object_or_404(Book, id=book_id)
    context = {'book': b, 'progress': progress}
    return render(request, 'book/book_title-Page.html', context)




def on_progress(view):
    def inner(request, book_id, **kwargs):
        book = get_object_or_404(Book, id=book_id) # мы НЕ хотим 2 раза идти в бд...
        try:
            progress = BookProgress.objects.get(book=book, user=request.user)
        except BookProgress.DoesNotExist:
            return redirect(reverse('book_main', kwargs={'book_id': book_id}))
        return view(request=request, progress=progress, book_id=book_id, **kwargs)
    return inner


# засунул логику создания програсса в мэйн функцию вместо доп декоратор
def book_main(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        progress = BookProgress.objects.get(book=book, user=request.user)
    except BookProgress.DoesNotExist:
        progress = BookProgress.start_progress(user=request.user, book=book)

    book = get_object_or_404(Book, id=book_id)
    page = progress.book_page
    links: list[tuple[any, bool], ...] = [
        (link, link.check_key_items(progress.inventory_items.all()))
        for link in page.pagelink_set.all()
    ]
    context = {'book': book, 'page': page, 'link_status_tuple': links , 'progress': progress}
    return render(request, 'book/book_page.html', context)


@on_progress
def go_to(request,progress, book_id, link_id): #реализовать привязку к линку т.к ?)
    page_link = get_object_or_404(PageLink, id=link_id)
    if (
        progress.book_page.id == page_link.from_page.id
        and
        page_link.check_key_items(progress.inventory_items.all())
    ): # обновление програсса если?
        progress.book_page = page_link.to_page
        progress.save()
    context = {'book_id': book_id}
    return redirect(reverse('book_main', kwargs=context))


@on_progress
def take_item(request, progress, book_id, item_id):
    item = get_object_or_404(Item, id=item_id)
    progress.inventory_items.add(item)
    context = {'book_id': book_id}
    return redirect(reverse('book_main', kwargs=context))


@on_progress
def drop_item(request, progress, book_id, item_id):

    return _return_to(book_id)


@on_progress
def saves(request, progress, book_id):
    """save page"""
    context = {'book': Book.objects.get(id=book_id),
               'progress': progress,
               'saves': progress.progresssave_set.all()}
    return render(request, 'book/saves.html', context)


@on_progress
def save_to(request, progress, book_id, save_id=None):
    """new/upd save"""
    save = progress.save_to(save_id=save_id)
    # upd/ save ?
    context = {'book_id': book_id, }
    return redirect(reverse('saves', kwargs=context))



@on_progress
def load_from(request, progress, book_id, save_id):
    progress.save_load(save_id)
    context = {'book_id': book_id}
    return redirect(reverse('saves', kwargs=context))
    # return HttpResponse('plug')


@on_progress
def delete_save(request, progress, book_id, save_id):
    save = get_object_or_404(ProgressSave, id=save_id)
    save.delete()
    return redirect(reverse('saves', kwargs={'book_id': book_id}))