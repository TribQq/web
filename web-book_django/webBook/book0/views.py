from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import *


def index(request):
    return render(request, 'book0/base.html', context={'books': Book.objects.all()})


def book(request,book_id):
    return render(request, 'book0/book.html', context={
        'book': get_object_or_404(Book, id=book_id)
    })


def book_page(request, book_id, page_id):
     return render(request, 'book0/page.html', context={
        'book':
            get_object_or_404(Book, id=book_id), 'page': get_object_or_404(BookPage, id=page_id)
    })


def page(request, book_id, page_id):
    return render(request, 'book0/page.html', context={
    'page': get_object_or_404(BookPage, book__id=book_id, id=page_id ) # # __ = ppep идём в соседнюю табл
    })



def plug(request,book_id,page_id):
    return HttpResponse('hi, it is plug')


