from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def plug(request):
    return HttpResponse('just plug')


def books_shelf(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book/book_shelf.html', context)


def book_titlePage(requst, book_id):
    book = get_object_or_404(Book.objects.filter(id=book_id))
    context = {'book': book}
    return render(requst, 'book/book_titlePage.html', context)


def book_page(request, book_id, page_id):
    page = get_object_or_404(BookPage.objects.filter(id=page_id))
    context = {'page': page}
    return render(request, 'book/book_page.html', context)