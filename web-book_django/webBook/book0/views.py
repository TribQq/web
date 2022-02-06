from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import *

from django.urls import reverse


def index(request):
    return render(request, 'book0/bookshelf.html', context={'books': Book.objects.all()})

# is_null() , вместо .id is Null т.к первый запрос это exists , а второй select , 1й просто эффективней (просто пометка для того ,что уже не юзается в этом контроллере)
def book(request, book_id):
    # is_first_page = Book.objects.all()[book_id-1].first_page
    # is_book = get_object_or_404(Book, id=book_id)
    # if is_first_page == None: # если поле first_page == null

    is_book = get_object_or_404(Book, id=book_id)
    if not is_book.first_page:
        return render(request, 'book0/book.html', context={
            'book': get_object_or_404(Book, id=book_id)
        })
    try:
        is_progress = BookProgress.objects.get(book=is_book, user=request.user)
    except BookProgress.DoesNotExist:
        is_progress = BookProgress.start_reading(user=request.user, book=is_book)
    return redirect(reverse('page', kwargs={'book_id':book_id, 'page_id': is_book.first_page.id}))
    # return redirect(reverse(plug)) # в плаг нельзя передавать агрументы .С url траблы (копнуть глубже) return redirect(reverse('plug', kwargs={'text': 'randomText'}))



def page(request, book_id, page_id):
    query = BookProgress.objects.filter(book=book_id, user=request.user,
                                        book_page=page_id) # чек параметров валидности ныненей страницы от прогресса (защита от хацкеров) $42-10
    if not query:
        return redirect(reverse('book', kwargs={'book_id': book_id}))
    return render(request, 'book0/page.html', context={
    'page': get_object_or_404(BookPage, book__id=book_id, id=page_id ) # # __ = ppep идём в соседнюю табл
    })


def plug(request, text='text'):
    return HttpResponse(text)

