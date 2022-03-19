from .views import *
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('plug/', plug, name='plug'),
    path('', TemplateView.as_view(template_name='index.html')), # /#/notes, /#/note/<:id>
]