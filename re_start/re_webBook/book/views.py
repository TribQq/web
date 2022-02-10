from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def plug(request):
    return HttpResponse('just plug')


def books_shelf(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/book_shelf.html', context)



def book_titlePage(request, book_id): # перенаправлять на фёрст мб + чек/создание прогресса
    b = get_object_or_404(Book, id=book_id)
    context = {'book': b}
    try:
        progress = BookProgress.objects.get(user=request.user, book=b)
    except BookProgress.DoesNotExist:
        if b.first_page is not None:
            progress = BookProgress.start_progress(user=request.user, book=b, page=b.first_page)
        else:
            page = get_object_or_404(BookPage, book_id=book_id, id=1)
            progress = BookProgress.start_progress(user=request.user, book=b, page=page)

    return render(request, 'book/book_title-Page.html', context)


def book_page(request, book_id, page_id): #чек/ создание прогресса/обновление/
    b = get_object_or_404(Book, id=book_id)
    p = get_object_or_404(BookPage, book_id=book_id, id=page_id)
    try:
        """n"""
    except:
        """n"""
    context = {'page': p}

    return render(request, 'book/book_page.html', context)