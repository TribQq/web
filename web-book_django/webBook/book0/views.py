from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import *


def index(request):
    return render(request, 'book0/base.html', context={'books': Book.objects.all()})


def book(request,book_id):
    return render(request, 'book0/book.html', context={
        'book': get_object_or_404(Book, id=book_id)
    })


def page(request, book_id, page_id):
    return render(request, 'book0/page.html', context={
        'page': get_object_or_404(BookPage, book__id=book_id, page_id=page_id)
    })