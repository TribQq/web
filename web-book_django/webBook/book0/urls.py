
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/<int:book_id>/', views.book),
    # path('book/<int:book_id>/page/<int:page_id>', views.book),
path('book/<int:book_id>/page/<int:page_id>', views.plug),
]
