from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import *


def plug(request):
    return HttpResponse('just plug')


def on_progress(view):
    def inner(request, book_id, **kwargs):
        b = get_object_or_404(Book, id=book_id) # мы НЕ хотим 2 раза идти в бд...
        try:
            progress = BookProgress.objects.get(user=request.user, book=b)
        except BookProgress.DoesNotExist:
            if b.first_page is not None:
                progress = BookProgress.start_progress(user=request.user, book=b, page=b.first_page)
            else:
                page = get_object_or_404(BookPage, book_id=book_id, id=1)
                progress = BookProgress.start_progress(user=request.user, book=b, page=page)
        # progress = 'plug'
        return view(request=request, progress=progress, book_id=book_id, **kwargs)
    return inner


# @on_progress
def books_shelf(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/book_shelf.html', context)


@on_progress
def book_titlePage(request, progress, book_id): # перенаправлять на фёрст мб + чек/создание прогресса
    b = get_object_or_404(Book, id=book_id)
    context = {'book': b, 'progress': progress}
    return render(request, 'book/book_title-Page.html', context)


@on_progress
def book_page(request, progress, book_id, page_id): #чек/ создание прогресса/обновление/
    p = get_object_or_404(BookPage, book_id=book_id, id=page_id)

    links_status: [tuple, ...] = [
        (link, link.check_key_items(inventory_items=progress.inventory_items.all()))
        for link in p.pagelink_set.all()
    ] #накалякать лапками самому


    context = {'page': p, 'progress': progress, 'link_status_tuple': links_status }
    return render(request, 'book/book_page.html', context)
    # add links checker

@on_progress
def take_item(request, progress, book_id, page_id, item_id):
    item = get_object_or_404(Item, id=item_id)
    progress.inventory_items.add(item)
    context = {'book_id': book_id, 'page_id': page_id}
    return redirect(reverse('book_page', kwargs=context))