from unicodedata import name
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('captcha/', include('captcha.urls')),
    path('bb/', include('bulletin_board.urls')),
    path('bookshelf/', include('bookshelf.urls')),
    path('', include('about_me.urls') ,name='about_me'),
    
    path('api_notesApp/', include('api_notesApp.urls')),
    path('api/', include('api_notesApp.urls')),
    path('notesApp/', include('react_notesApp.urls'))

]

handler404 = "mysite.views.page_not_found_view"
# handler404 = "about_me.views.about_main"

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # маршрут для обработки выгруженных файлов

