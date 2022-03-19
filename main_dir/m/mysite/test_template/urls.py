from django.urls import path

from .views import *


urlpatterns = [
   path('onlyScroll/', onlyScroll, name='onlyScroll'),
   path('', bookshelf, name='bookshelf'),
   path('book_pages', book_pages, name='book_pages'),
]
