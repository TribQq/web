from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.views.decorators.cache import never_cache

from django.conf.urls import url

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('captcha/', include('captcha.urls')),
    path('bb/', include('bulletin_board.urls')),
    path('bookshelf/', include('bookshelf.urls')),
    path('', include('about_me.urls') ,name='about_me'),
    
    path('api_notesApp/', include('api_notesApp.urls')),
    path('api/', include('api_notesApp.urls')),
    path('notesApp/', include('react_notesApp.urls')),
       
    path('accounts/profile/', view_profile, name='view_profile'),
] 


handler404 = "mysite.views.page_not_found_view"

if settings.DEBUG:
    from django.contrib.staticfiles.views import serve
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # маршрут для обработки выгруженных файлов
else: # only for heroku , if deploy + nginx/apache need refactor
    from django.views.static import serve as serve
    urlpatterns.extend([
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),   
    ])
    
    
