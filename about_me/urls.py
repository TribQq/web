from unicodedata import name
from django.urls import path

from .views import *

app_name = 'about_me'
urlpatterns = [
   path('', about_main, name='about_main'),
   path('alt/', alt_about_me, name='alt_about_me'),
   path('404/', handler_404, name='handler_404'),
]