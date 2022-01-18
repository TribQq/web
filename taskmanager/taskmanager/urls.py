
from django.contrib import admin
from django.urls import path,include

urlpatterns = [ #urlpatterns не трож сломаешь сук
    path('admin/', admin.site.urls),
    path('', include('main_application.urls_s')) # переход на главую странику . это основное юрл файл
]


