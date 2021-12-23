from django.urls import path
from .views import *

urlpatterns=[
    path('add',BBCreateView.as_view(),name='add'),
    path('<int:rubric_id>/', by_rubric , name='by_rubric'),  # указываем элемент класса(рубрику) как маршрут для функции by_rubric
    path('',index , name='index'),
    # path('1/',index_1),
]