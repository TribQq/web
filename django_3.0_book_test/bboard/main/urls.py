from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('account/profile/', profile, name='profile'), # передаёт функции из views нужные значения(+ чекает)
    path('account/logout/', BBLogoutView.as_view(), name='logout'),
    path('account/login/', BBLoginView.as_view() , name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
