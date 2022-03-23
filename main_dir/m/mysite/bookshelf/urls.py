from django.urls import path

from .views import *


urlpatterns = [
   path('plug/', view_plug, name='plug'),
   path('onlyScroll/', view_onlyScroll, name='onlyScroll'),

   path('', view_bookshelf, name='view_bookshelf'),
   path('book/<int:book_id>/', view_read_book, name='view_read_book'),
   
   path('book_main/<int:book_id>/go_to/<int:link_id>', view_go_to, name='view_go_to'),
   
      
   path('book_main/<int:book_id>/take_item/<int:item_id>', view_take_item, name='view_take_item'),
   path('book_main/<int:book_id>/drop_item/<int:item_id>', view_drop_item, name='view_drop_item'),
   path('book_main/<int:book_id>/take_back_item/<int:item_id>', view_take_back_item, name='view_take_back_item'),
   

   
   path('book_main/<int:book_id>/add_note/', view_add_note, name='view_add_note'),
   path('book_main/<int:book_id>/toggle_pin/<int:note_id>/', view_toggle_pin, name='view_toggle_pin'),
   path('book_main/<int:book_id>/delete_note/<int:note_id>', view_delete_note, name='view_delete_note'),
   path('book/<int:book_id>/update_note/<int:note_id>/', view_update_note, name='view_update_note'),


   path('book_main/<int:book_id>/saves', view_saves, name='view_saves'),
   path('book_main/<int:book_id>/new_save/', view_save_to, name='view_new_save'),
   path('book_main/<int:book_id>/save_to/<int:save_id>', view_save_to, name='view_save_to'),
   path('book_main/<int:book_id>/load_from/<int:save_id>', view_load_from, name='view_load_from'),
   path('book_main/<int:book_id>/delete_save/<int:save_id>', view_delete_save, name='view_delete_save'),

   path('book_main/<int:book_id>/drop_progress', view_drop_progress, name='view_drop_progress'),


]