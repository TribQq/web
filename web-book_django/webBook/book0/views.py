from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from django.urls import reverse

from graphviz import Digraph

from .models import *
from book0 import book_map


def _return_to(book_id):
    return redirect(reverse('book', kwargs={'book_id': book_id}))


def on_progress(view):
    def inner(request, book_id, **kwargs):
        try:
            progress = BookProgress.objects.get(book=book_id, user=request.user)
        except BookProgress.DoesNotExist:
            return redirect(reverse('book', kwargs={'book_id': book_id}))
        return view(request=request, progress=progress, book_id=book_id,
                    **kwargs)  # генерируем прогресс для каждой функции с помощью декоратоа

    return inner


def index(request):
    return render(request, 'book0/bookshelf.html', context={'books': Book.objects.all()})


# @on_progress
def book(request, book_id: int) -> render:
    book = get_object_or_404(Book, id=book_id)
    if not book.first_page:
        raise ValueError('Book {0.id} has not a first page!')
    try:
        progress = BookProgress.objects.get(book=book, user=request.user)
    except BookProgress.DoesNotExist:
        progress = BookProgress.start_reading(user=request.user, book=book)

    page = progress.book_page

    links: list[tuple[any, bool], ...] = [
        (link, link.check_items(list(progress.items.all())))
        for link in page.pagelink_set.all()
    ]
    return render(request, 'book0/page.html',
                  context={
                      'page': page,  # # __ = ppep идём в соседнюю табл
                      'progress': progress,
                      'link_status_tuples': links,
                      'page_items': page.items.exclude(id__in=progress.items.only('id'))
                  })


@on_progress
def go_to(request, progress, book_id: int, pagelink_id: int):
    link = get_object_or_404(PageLink, id=pagelink_id)
    if (
        link.from_page.id == progress.book_page.id # no upd problem idk ( (fixed) fail id luil)
        and
        link.check_items(progress.items.all())
    ):
        progress.book_page = link.to_page # если проходит if , то ресэйвим прогресс иначе не проходит оновление прогресса и -> не ченджится страница
        progress.save()
    return _return_to(book_id=book_id)


@on_progress
def take(request, progress, book_id, item_id):
    item = get_object_or_404(Item, id=item_id)
    if (
        item in progress.book_page.items.all()
    ):
        progress.items.add(item)
    return _return_to(book_id=book_id)


@on_progress
def saves(request, progress, book_id):
    saves = progress.progresssave_set.all().order_by('-updated_at')
    return render(request, 'book0/saves.html',
                  context={
                      'book': progress.book,
                      'saves': saves,
                  })


@on_progress
def save_to(request, progress, book_id, save_id=None): # None for new_save
    progress.save_to(save_id)
    return redirect(reverse('saves', kwargs={'book_id': book_id}))


@on_progress
def load_from(request, progress, book_id, save_id):
    progress.load_from(save_id)
    return redirect(reverse('saves', kwargs={'book_id': book_id}))


@on_progress
def save_delete(request, progress, book_id, save_id):
    ProgressSave.objects.get(id=save_id).delete()
    return redirect(reverse('saves', kwargs={'book_id': book_id}))


def plug(request, text='text'):
    return HttpResponse(text)


def view_book_map(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return FileResponse(book_map.book_map(book), filename='map.svg')

