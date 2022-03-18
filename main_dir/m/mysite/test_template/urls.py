from django.urls import path

from .views import *


urlpatterns = [
   path('', baic_template, name='paper_scroll'),
   path('note/', template_with_text, name='note_text')
]