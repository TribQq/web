import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-78z-a3p@wo60zip=b5h%c!4yeg^$55!uo30s4cx2yh#8s*z^)$'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig', # приложение
    'bootstrap4',  # програмное ядро библы django-bootstrap4
    'django_cleanup',
    # (удаляет выгруженные файлы после удаления хранящих их записеймоделей mb need django_cleanup.apps.CleanupConfig'
    'easy_thumbnails',  # создает миниатюры
    'captcha', # каптча комментов
    'rest_framework', #
    'corsheaders',
    'api.apps.ApiConfig', # приложение

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.middlewares.bboard_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'bboard.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'bboard.data',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'main.AdvUser'  # переназначаем дефолтную модель юзера на модель из...

EMAIL_PORT = 725
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Параметр EMAIL_BACKEND указывает класс, используемый для отправки email-ов.

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THUMBNAIL_ALIASES = {'': {
    'default': {'size': (96, 96),
                'crop': 'scale'}, }, }  # настройки плагин(ов)
THUMBNAIL_BASEDIR = 'thumbnails'

# и, настройки,разрешающие доступ к веб-службе с любого домена:
CORS_ORIGIN_ALLOW_ALL = True
CORS_URL_REGEX = r'^/api/.*$'
