from django.urls import path

from .views import *


urlpatterns = [
   path('', about_main, name='about_main'),

]