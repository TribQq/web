from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

def onlyScroll(request):
    return render(request, 'layout/scroll_basic.html')


def bookshelf(request):
    return render(request, 'bookshelf.html')



def book_pages(request):
    return render(request, 'book_pages.html')


# def try_test(request):
#     return render(request, '3try.html')



# def single_test(request):
#     return render(request, '2read_book.html')


