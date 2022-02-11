from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('book/<int:book_id>/', views.book, name='book'),
    path('book/<int:book_id>/page/<int:page_id>', views.page, name='page'),
    path('book/<int:book_id>/page/<int:page_id>/take/<int:item_id>/', views.take, name='take'),
    path('plug', views.plug, name='plug'),
]


