from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/<int:book_id>/go/<int:pagelink_id>', views.go_to, name='go_to'),
    path('book/<int:book_id>/take/<int:item_id>/', views.take, name='take'),
    path('book/<int:book_id>/saves', views.saves, name='saves'),
    path('book/<int:book_id>/saves/saves/new', views.save_to, name='save_new'), #new save
    path('book/<int:book_id>/saves/save_to/<int:save_id>', views.save_to, name='save_to'),
    path('book/<int:book_id>/saves/load_from/<int:save_id>', views.load_from, name='load_from'),

    path('book/<int:book_id>/map.svg', views.view_book_map, name='view_book_map'),
    path('plug', views.plug, name='plug'),
]


