from django.urls import path

from .views import *


urlpatterns = [
   path('plug/', plug, name='plug'),
   path('booksShelf/', books_shelf, name='book_shelf'),
   path('book/<int:book_id>/', book_titlePage, name='book_titlePage'), #/<int:book_id>
   path('book/<int:book_id>/page/<int:page_id>', book_page, name='book_page'),
   path('book/<int:book_id>/page/<int:page_id>/item/<int:item_id>', take_item, name='take_item'),

   path('book_main/<int:book_id>/', book_main, name='book_main'),
   path('book_main/<int:book_id>/go_to/<int:link_id>', go_to, name='go_to'),
   path('book_main/<int:book_id>/item/<int:item_id>', go_take_item, name='go_take_item'),

]

# {% url 'go_to' page.book_id link.to_page.id %}
