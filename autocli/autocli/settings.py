"""
Django settings for autocli project.
Generated by 'django-admin startproject' using Django 4.1.
"""

# Django Import:
from pathlib import Path

# Jazzmin Import:
from .jazzmin import JAZZMIN_SETTINGS

"""
python manage.py dumpdata --format yaml --exclude=auth --exclude=admin --exclude=contenttypes --exclude=sessions --output test
celery -A autocli worker -Q collect_data -l INFO
python manage.py loaddata --format yaml copy.yaml
"""

# Build paths inside the project like this:
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING:
SECRET_KEY = 'django-insecure-velu4t6^w34z=kzx2%j2emu7qfeovi1j4iiy-c8h-&#u&9gvkv'

# SECURITY WARNING:
DEBUG = True
ALLOWED_HOSTS = []

# Application definition:
INSTALLED_APPS = [
    # Django Jazzmin:
    'jazzmin',
    
    # Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Celery and channels pps:
    'django_celery_beat',
    'channels',
    'django_filters',
    'rest_framework',

    # AutoCLI system apps:
    # 'system.administration.apps.AdministrationConfig',
    'system.settings.apps.SettingsConfig',

    # AutoCLI network apps:
    'network.automation.apps.AutomationConfig',
    'network.datasets.apps.DatasetsConfig',
    'network.inventory.apps.DevicesConfig',
    'network.tags.apps.TagsConfig',
    'network.updates.apps.UpdatesConfig',

    # AutoCLI messages apps:
    'messages.notifications.apps.NotificationsConfig',
    'messages.changes.apps.ChangesConfig',
    'messages.logger.apps.LoggerConfig',

    # AutoCLI other apps:
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'autocli.urls'
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
            ],
        },
    },
]

# WSGI and ASGI configuration:
WSGI_APPLICATION = 'autocli.wsgi.application'
ASGI_APPLICATION = 'autocli.asgi.application'

# Celery configuration:
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Channels configuration:
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],
        },
    },
}

# Database configuration:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db1.sqlite3',
    }
}

# docker run --name AutoCLI-DB -p 5005:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=autocli postgres
# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'autocli',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': '127.0.0.1',
#         'PORT': 5005,
#     }
# }

# Default user model:
# AUTH_USER_MODEL = 'administration.Administrator'

# Password validation:
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

# Internationalization:
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files:
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath('static'),
    BASE_DIR.joinpath('media'),
]
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

# Templates:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'),
            BASE_DIR.joinpath('static'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin settings:
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
}

# Change log models:
CHANGE_LOG_MODELS = [
    ('inventory', 'Device'),
    ('inventory', 'DeviceType'),
    ('inventory', 'DeviceTypeTemplate'),
    ('inventory', 'Group'),
    ('inventory', 'Credential'),
    ('tags', 'Tag'),
]

# API:
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}
