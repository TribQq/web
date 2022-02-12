from django.urls import path

from .views import *


urlpatterns = [
   path('plug/', plug, name='plug'),
   path('booksShelf/', books_shelf, name='book_shelf'),
   path('book/<int:book_id>/', book_titlePage, name='book_titlePage'), #/<int:book_id>
   path('book/<int:book_id>/page/<int:page_id>', book_page, name='book_page'),
   path('book/<int:book_id>/page/<int:page_id>/item/<int:item_id>', take_item, name='take_item'),

]
