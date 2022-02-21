from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/<int:book_id>/go/<int:pagelink_id>', views.go_to, name='go_to'),
    path('book/<int:book_id>/take/<int:item_id>/', views.take, name='take'),
    path('book/<int:book_id>/drop_item/<int:item_id>/', views.drop_item, name='drop_item'),
    path('book/<int:book_id>/take_back/<int:dropped_item_id>/', views.take_back_item, name='take_back'),

    path('book/<int:book_id>/add_note/', views.add_note, name='add_note'),
    path('book/<int:book_id>/remove_note/<int:note_id>/', views.remove_note, name='remove_note'),
    path('book/<int:book_id>/update_note/<int:note_id>/', views.update_note, name='update_note'),
    path('book/<int:book_id>/toggle_pin/<int:note_id>/', views.toggle_pin, name='toggle_pin'),


    path('book/<int:book_id>/saves', views.saves, name='saves'),
    path('book/<int:book_id>/saves/saves/new', views.save_to, name='save_new'), #new save
    path('book/<int:book_id>/saves/save_to/<int:save_id>', views.save_to, name='save_to'),
    path('book/<int:book_id>/saves/load_from/<int:save_id>', views.load_from, name='load_from'),
    path('book/<int:book_id>/saves/save_delete/<int:save_id>', views.save_delete, name='save_delete'),

    path('book/<int:book_id>/map.svg', views.view_book_map, name='view_book_map'),
    path('plug', views.plug, name='plug'),
]


