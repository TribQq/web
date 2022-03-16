import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%+$+reas1f7vm*xep@t#1-2gs&ci^ptq_m-bj5__pnm&cf5j3y'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bulletin_board.apps.BulletinConfig',
    'bootstrap4',  # програмное ядро библы django-bootstrap4
    'django_cleanup',# (удаляет выгруженные файлы после удаления хранящих их записей моделей mb need django_cleanup.apps.CleanupConfig'
    'easy_thumbnails',  # создает миниатюры
    'captcha',  # каптча комментов
    'rest_framework',
    'corsheaders',
    # 'api.apps.ApiConfig', # приложение

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware', #
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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
                'bulletin_board.middlewares.bboard_context_processor', #
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mysite_db',
            'USER': 'petuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
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

AUTH_USER_MODEL = 'bulletin_board.AdvUser'

EMAIL_PORT = 725
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Параметр EMAIL_BACKEND указывает класс, используемый для отправки email-ов.

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THUMBNAIL_ALIASES = {
    '': {
        'default': {
            'size': (96, 96),
            'crop': 'scale'}
        , }
    , }  # настройка thumbnail`s

THUMBNAIL_BASEDIR = 'thumbnails'

# доступ к веб-службе с любого домена
CORS_ORIGIN_ALLOW_ALL = True
CORS_URL_REGEX = r'^/api/.*$'
