from django.urls import path

from .views import *


urlpatterns = [
   path('plug/', view_plug, name='plug'),
   path('onlyScroll/', view_onlyScroll, name='onlyScroll'),

   path('', view_bookshelf, name='bookshelf'),
   path('book/<int:book_id>/', view_read_book, name='read_book'),
   path('book/<int:book_id>', view_read_book, name='read_book_anchor'),
   
   path('book_main/<int:book_id>/go_to/<int:link_id>', go_to, name='go_to'),
   
      
   path('book_main/<int:book_id>/take_item/<int:item_id>', take_item, name='take_item'),
   path('book_main/<int:book_id>/drop_item/<int:item_id>', drop_item, name='drop_item'),
   path('book_main/<int:book_id>/take_back_item/<int:item_id>', take_back_item, name='take_back_item'),
   

   
   path('book_main/<int:book_id>/add_note/', view_add_note, name='add_note'),
   path('book_main/<int:book_id>/toggle_pin/<int:note_id>/', view_toggle_pin, name='toggle_pin'),
   path('book_main/<int:book_id>/delete_note/<int:note_id>', view_delete_note, name='delete_note'),
      path('book/<int:book_id>/update_note/<int:note_id>/', view_update_note, name='update_note'),


   path('book_main/<int:book_id>/saves', view_saves, name='saves'),
   path('book_main/<int:book_id>/new_save/', view_save_to, name='new_save'),
   path('book_main/<int:book_id>/save_to/<int:save_id>', view_save_to, name='save_to'),
   path('book_main/<int:book_id>/load_from/<int:save_id>', view_load_from, name='load_from'),
   path('book_main/<int:book_id>/delete_save/<int:save_id>', view_delete_save, name='delete_save'),




]