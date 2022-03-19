from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('bb/', include('bulletin_board.urls')),
    path('bookshelf/', include('bookshelf.urls')),
    path('aboutMe/', include('about_me.urls')),

    path('api_notesApp/', include('api_notesApp.urls')),
    path('notes/', include('react_notesApp.urls'))
    # path('', TemplateView.as_view(template_name='react_frontend/notesApp_build_react/index.html')), # /#/notes, /#/note/<:id>

]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # маршрут для обработки выгруженных файлов

