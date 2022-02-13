from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/<int:book_id>/go/<int:pagelink_id>', views.go_to, name='go_to'),
    path('book/<int:book_id>/take/<int:item_id>/', views.take, name='take'),
    path('book/<int:book_id>/map.svg', views.view_book_map, name='view_book_map'),
    path('plug', views.plug, name='plug'),
]


