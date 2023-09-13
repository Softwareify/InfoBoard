import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = bool(int(os.getenv("DEBUG")))

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(" ")

IS_PRODUCTION = bool(int(os.getenv("IS_PRODUCTION")))

# CMS
IS_CMS = bool(int(os.getenv("IS_CMS")))

# FRONT
IS_FRONT = bool(int(os.getenv("IS_FRONT")))

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # "django_elasticsearch_dsl",
    # "django_elasticsearch_dsl_drf",
    "authentication",
    "cms",
    "front",
    "content",
    "content.page",
    "content.page_structure",
    "snippets",
    "snippets.wyswig",
    "snippets.video_snippet",
    "ckeditor",
    "elastic_search",
    "tinymce",
    "modules",
    "modules.video",
    "publisher",
    "content.page_status",
]

# ELASTICSEARCH_INDEX_NAMES = {
#     "pages.page": "pages",
# }

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "ORDERING_PARAM": "ordering",
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{os.getenv('REDIS_HOST')}:6379/",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Elasticsearch configuration
# ELASTICSEARCH_DSL = {
#     "default": {"hosts": f"{os.getenv('ES_HOST')}:9200"},
# }

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "infoboard.middlewares.VideoMergeMiddleware",
]

ROOT_URLCONF = "infoboard.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "infoboard.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    },
    "public": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME_PUBLIC"),
        "USER": os.environ.get("DB_USERNAME_PUBLIC"),
        "PASSWORD": os.environ.get("DB_PASSWORD_PUBLIC"),
        "HOST": os.environ.get("DB_HOST_PUBLIC"),
        "PORT": os.environ.get("DB_PUBLIC_PORT"),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

STATICFILES_DIRS = (BASE_DIR / "static",)

LANGUAGE_CODE = "pl-pl"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "mediafiles"
MEDIA_URL = "mediafiles/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
]

CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS").split(" ")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")

MAX_RETRIES = 5
