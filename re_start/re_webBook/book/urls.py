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

   path('book_main/<int:book_id>/saves', saves, name='saves'),
   path('book_main/<int:book_id>/new_save/', save_to, name='new_save'),
   path('book_main/<int:book_id>/save_to/<int:save_id>', save_to, name='save_to'),
   path('book_main/<int:book_id>/load_from/<int:save_id>', load_from, name='load_from'),

]

# {% url 'go_to' page.book_id link.to_page.id %}
