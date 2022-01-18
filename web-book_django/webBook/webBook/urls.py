
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('book0.urls')),
    path('admin/', admin.site.urls),
]
