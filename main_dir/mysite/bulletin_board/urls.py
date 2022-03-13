from django.urls import path
from .views import *


urlpatterns = [
    path('', index1),
    path('<str:page>/', other_page, name='other'),
]