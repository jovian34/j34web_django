from dotenv import load_dotenv
from pathlib import Path
from datetime import date
import os

load_dotenv()
today = date.today()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DEVELOP")))

if not bool(int(os.environ.get("DEVELOP"))):
    ALLOWED_HOSTS = [
        "jovian34.com",
        "www.jovian34.com",
        "137.184.100.121",
    ]

else:
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
    ]


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

INSTALLED_APPS = [
    "django_project.apps.DjangoProjectConfig",
    "j34main.apps.J34MainConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "django_project/templates"],
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

WSGI_APPLICATION = "django_project.wsgi.application"


if bool(int(os.environ.get("DEVELOP"))):
    host_name = "localhost"
else:
    host_name = "localhost"
    # host_name = "cyllene.jovian34.com"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "j34web_django",
        "USER": "j34web_django",
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": host_name,
        "PORT": "5432",
    }
}

if DEBUG:
    log_level = "DEBUG"
else:
    log_level = "WARNING"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": log_level,
            "class": "logging.FileHandler",
            "filename": f"{BASE_DIR}/logs/{today}_logging.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": log_level,
            "propagate": True,
        },
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


# Registration

LOGIN_REDIRECT_URL = "index"

LOGOUT_REDIRECT_URL = "index"


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Indiana/Indianapolis"

USE_I18N = True

USE_TZ = True


# Static and Security

STATIC_URL = "/static/"

if not bool(int(os.environ.get("DEVELOP"))):
    # added due to security warnings
    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 9999

    SECURE_SSL_REDIRECT = True

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

    SESSION_COOKIE_SECURE = True

    STATIC_ROOT = os.path.join(BASE_DIR, "django_project/static/")

project_version = "0.7.1"  # update Python to 3.12.5 and Django to 5.1 ATP 2024-08-09
os.environ.setdefault("PROJECT_VERSION", project_version)
