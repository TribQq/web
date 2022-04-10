from django.urls import path
from django.views.generic import TemplateView

app_name = 'react_notesApp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'),name="notesApp"), # Hashrouter http://127.0.0.1:8000/notes/#/notes
]