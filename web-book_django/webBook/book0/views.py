from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse

from graphviz import Digraph

from .models import *

from django.urls import reverse


def on_progress(view):
    def inner(request, book_id, **kwargs):
        try:
            progress = BookProgress.objects.get(book=book_id, user=request.user)
        except BookProgress.DoesNotExist:
            return redirect(reverse('book', kwargs={'book_id': book_id}))
        return view(request=request, progress=progress, book_id=book_id, **kwargs) # генерируем прогресс для каждой функции с помощью декоратоа

    return inner


def index(request):
    return render(request, 'book0/bookshelf.html', context={'books': Book.objects.all()})


@on_progress
def book(request, progress, book_id):
    # b = get_object_or_404(Book, id=book_id)
    # if not b.first_page:
    #     return render(request, 'book0/book.html', context={
    #         'book': get_object_or_404(Book, id=book_id)
    #     })
    # try:
    #     progress = BookProgress.objects.get(book=b, user=request.user)
    # except BookProgress.DoesNotExist:
    #     progress = BookProgress.start_reading(user=request.user, book=b)
    return redirect(reverse('page', kwargs={'book_id': book_id, 'page_id': progress.book_page.id, }))
    # return redirect(reverse(plug)) # в плаг нельзя передавать агрументы .С url траблы (копнуть глубже) return redirect(reverse('plug', kwargs={'text': 'randomText'}))


@on_progress
def page(request, progress, book_id, page_id):
    page = get_object_or_404(BookPage, book__id=book_id, id=page_id)
    progress.book_page = page
    progress.save()

    links = [
        (
            link, link.check_items(list(progress.items.all()) # (link , status_link)
                                   )
        )
        for link in page.pagelink_set.all()
    ]
    return render(request, 'book0/page.html', context={
        'page': page,  # # __ = ppep идём в соседнюю табл
        'progress': progress,
        'link_status_tuples': links,
        'page_items': page.items.exclude(id__in=progress.items.only('id'))
    })


@on_progress
def take(request, progress, book_id, page_id, item_id):
    item = get_object_or_404(Item, id=item_id)
    progress.items.add(item)
    return redirect(reverse('page', kwargs={'book_id': book_id, 'page_id': page_id, }))


def plug(request, text='text'):
    return HttpResponse(text)


def view_book_map(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    graph = Digraph('Map', filename='map.gv', directory='tmp/') #, directory='/tmp'
    for link in PageLink.objects.filter(from_page__book_id=book_id).all(): # фильтруем page link`и выбранной книги
        graph.edge(link.from_page.title, link.to_page.title) # добавляем их в граф

    # graph.edge('A', 'B') # test graph
    graph.render(quiet=True, view=False, format='svg') # методы graphiviz`a
    return FileResponse(open('tmp/map.gv.svg', 'rb')) # метод для открытыия файлов
