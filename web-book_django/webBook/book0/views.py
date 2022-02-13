from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from django.urls import reverse


from graphviz import Digraph

from .models import *


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
    assert book.first_page, 'cant_get_book_Error'
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



def plug(request, text='text'):
    return HttpResponse(text)


def view_book_map(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    g = Digraph('Map', filename='map.gv', directory='/tmp')

    def pid(page):
        return 'page_{id}'.format(id=page.id)

    for page in book.bookpage_set.all():
        g.node(
            pid(page),
            label='\n'.join(
                [str(page.id), page.title] + [
                    i.name for i in page.items.all()
                ]
            ),
            tooltip=page.body,
            href='/admin/book0/bookpage/{}/change'.format(page.id),
        )

    for link in PageLink.objects.filter(
            from_page__book_id=book_id,
    ).all():
        g.edge(pid(link.from_page), pid(link.to_page), label='\n'.join(
            [str(link.id), link.name[:10]] + [
                i.name for i in link.items.all()
            ]),
               labeltooltip=link.name,
               labelhref='/admin/book0/pagelink/{}/change'.format(link.id),
               )

    g.render(quiet=True, view=False, format='svg')
    return FileResponse(open('/tmp/map.gv.svg', 'rb'))
