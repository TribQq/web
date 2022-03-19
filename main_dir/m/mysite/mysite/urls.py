from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('bb/', include('bulletin_board.urls')),
    path('bookShelf/', include('bookshelf.urls')),
    path('AboutMe/', include('about_me.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # маршрут для обработки выгруженных файлов

