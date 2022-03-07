from django.urls import path
from .views import *

urlpatterns = [

    path('', getRoutes, name='getRoutes'),
    path('notes/', get_notes, name='getNotes'),
    path('note/<int:note_id>/', get_note, name='get_note'),
    
    path('note/<int:note_id>/update', note_update, name='get_update'),
    path('note/<int:note_id>/delete', note_delete, name='note_delete'),
    path('note/note_create', note_create, name='note_create'),
]