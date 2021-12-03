from django.urls import path
from . import views     #а поч тут точка работает дачёзанах я ебал


urlpatterns = [
    path('', views.index_x , name = 'home_page'), # ,path ('about-us' , views.index_x)
    path('about_us' , views.about_t, name = 'about_page'), #+адрес about_us
    path(' create_task', views.create_task, name = 'new_task'),
]

