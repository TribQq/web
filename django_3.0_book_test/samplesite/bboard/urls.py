from django.urls import path
from .views import *

urlpatterns=[# на этот модуль ссылаются шаблоны хтмл для взятия тегов + внешний urls для взятия маршрутов
    path('add',BBCreateView.as_view(),name='add'), # к классу BBCreteView с методом as_veiw
    path('<int:rubric_id>/', by_rubric , name='by_rubric'),  # указываем элемент класса(Id рубрики) как маршрут для функции by_rubric
    path('',index , name='index'),
    # path('1/',index_1),
]