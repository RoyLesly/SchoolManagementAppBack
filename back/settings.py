from pathlib import Path
import os
from django.conf import settings
from datetime import timedelta
from import_export.formats.base_formats import CSV, XLSX

IMPORT_FORMATS = [CSV, XLSX]
EXPORT_FORMATS = [CSV, XLSX]

# load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
CORS_ALLOW_ALL_ORIGINS = True
SECRET_KEY = 'django-insecure-voq(is89b&38ntkz1xse#tbl8%er&+gn=3&1r$_5s_9jy2so)+'
DEBUG = True

ALLOWED_HOSTS = [ "*", "http://localhost", "brains.localhost", "test.localhost"]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "user_control.CustomUser"

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "back.custom_methods.custom_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": ('rest_framework_simplejwt.authentication.JWTAuthentication',),
}

SHARED_APPS = [
    'django_tenants',  # mandatory
    'tenant',
    'jazzmin',
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_rest_passwordreset',
    'import_export',
    # 'advanced_filters',
    # 'django_crontab',
    # 'dbbackup',

    # FOR HIGHER
    'higher_control.user_control.apps.UserControlConfig',
    'higher_control.app_control.apps.AppControlConfig',
    'higher_control.fees_control.apps.FeesControlConfig',
    'higher_control.noti_control.apps.NotiControlConfig',
    #'higher_control.time_control.apps.TimeControlConfig',
    # FOR SECONDARY
    'secondary_control.sec_user_control.apps.SecUserControlConfig',
    'secondary_control.sec_app_control.apps.SecAppControlConfig',
    'secondary_control.sec_fees_control.apps.SecFeesControlConfig',
    # FOR PRIMARY
    'primary_control.prim_user_control.apps.PrimUserControlConfig',
    'primary_control.prim_app_control.apps.PrimAppControlConfig',
    'primary_control.prim_fees_control.apps.PrimFeesControlConfig',
    # FOR VOCATIONAL
]

TENANT_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    # 'django.contrib.sessions',
    'django.contrib.messages',

    # tenant-specific apps
    'jazzmin',
    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # FOR HIGHER
    'higher_control.user_control.apps.UserControlConfig',
    'higher_control.app_control.apps.AppControlConfig',
    'higher_control.fees_control.apps.FeesControlConfig',
    'higher_control.noti_control.apps.NotiControlConfig',
    'higher_control.time_control.apps.TimeControlConfig',
    # FOR SECONDARY
    'secondary_control.sec_user_control.apps.SecUserControlConfig',
    'secondary_control.sec_app_control.apps.SecAppControlConfig',
    'secondary_control.sec_fees_control.apps.SecFeesControlConfig',
    # FOR PRIMARY
    'primary_control.prim_user_control.apps.PrimUserControlConfig',
    'primary_control.prim_app_control.apps.PrimAppControlConfig',
    'primary_control.prim_fees_control.apps.PrimFeesControlConfig',

    # FOR VOCATIONAL

    'django_rest_passwordreset',
    'import_export',
    'advanced_filters',
    'django_crontab',
    # 'dbbackup',
]

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

# DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
# DBBACKUP_STORAGE_OPTIONS = {'location': '/home/cp2281266p21/public_html/back/database/'}

# CRONJOBS = [
#     ('30 23 * * *', 'back.dbcron.db_cron_backup')
# ]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    # custom tenant middleware
    'back.middleware.TenantMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TENANT_MODEL = "tenant.Tenant"
TENANT_DOMAIN_MODEL = "tenant.Domain"

ROOT_URLCONF = 'back.urls'
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

WSGI_APPLICATION = 'back.wsgi.application'
ASGI_APPLICATION = 'back.asgi.application'

CHANNEL_LAYERS = {
    # "default": { "BACKEND": "channels.layers.InMemoryChannelLayer" },
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [('back.econneq.com', 6379), ('back.econneq.com', 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'estudent', # 'estudents'
        'USER': 'postgres',  # 'postgres',
        'PASSWORD': 'Rjlink75',  # 'Admin',
        'HOST': '127.0.0.1',  # '37.60.235.58',
        'PORT': '5432'
    }
}

DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = '/home/cp2281266p21/public_html/back/static'

DJANGO_REST_PASSWORDRESET_TOKEN_CONFIG = {
    "CLASS": "django_rest_passwordreset.tokens.RandomNumberTokenGenerator",
    "OPTIONS": {
        "min_length": 5,
        "max_length": 5
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "mail.st-joan.com"
EMAIL_HOST_USER = "support@st-joan.com"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = "S5ul5Pygi9%1"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

# CSRF_TRUSTED_ORIGINS = [ "http://localhost", "http://brains.localhost", ]
# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = False

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=12),
    "ROTATE_REFRESH_TOKENS": False,
    "TOKEN_OBTAIN_SERIALIZER": "user_control.serializers.MyTokenObtianPairSerializer",
    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
}

JAZZMIN_SETTINGS = {
    "order_with_respect_to": ['user_control', 'app_control', "django_rest_passwordreset", "tenant",
                              "fees_control", "time_control", ],

    "site_brand": "Econneq School",

    "welcome_sign": "Best Choice University",

    "copyright": "Econneq Systems",
}
