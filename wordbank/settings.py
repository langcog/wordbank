# Django settings for wordbank project.
import os

SITE_DIR = (os.path.join(os.path.dirname(__file__), "..")).replace("\\", "/")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEV = os.path.isfile(os.path.join(SITE_DIR, "dev"))
DEBUG = True
if DEV:
    DEBUG = True

ADMINS = (("Mika Braginsky", "mikabr@stanford.edu"),)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# SHINY_SERVER_URL = "https://wordbank-shiny.com"
SHINY_SERVER_URL = "https://langcog.shinyapps.io"

MANAGERS = ADMINS

if "DATABASE_NAME" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ["DATABASE_NAME"],
            "USER": os.environ["DATABASE_USER"],
            "PASSWORD": os.environ["DATABASE_PASSWORD"],
            "HOST": os.environ["DATABASE_HOSTNAME"],
            "PORT": os.environ["DATABASE_PORT"],
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "wordbank",
            "USER": "wordbankadmin",
            "PASSWORD": "password",
            "HOST": "localhost",
            "PORT": 3306,
        }
    }


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
from socket import gethostname, gethostbyname  # For AWS Healthchecker

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".wordbank.stanford.edu",
    ".us-west-2.elasticbeanstalk.com"
    # gethostname(), gethostbyname(gethostname()), # AWS hosts for Healthchecker
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "America/Chicago"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# FILE_UPLOAD_PERMISSIONS = 0644

MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "media")
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")


# Make this unique, and don't share it with anybody.
from django.utils.crypto import get_random_string


def generate_secret_key(fname):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    f = open(fname, "w")
    f.write("SECRET_KEY = '%s'\n" % get_random_string(50, chars))


try:
    from .secret_key import *
except ImportError:
    SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(SETTINGS_DIR, "secret_key.py"))
    from .secret_key import *

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "wordbank.urls"

WSGI_APPLICATION = "wordbank.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates/",
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
            os.path.join(os.path.dirname(__file__), "..", "templates").replace(
                "\\", "/"
            ),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "debug": DEBUG,
        },
    },
]

INSTALLED_APPS = [
    "wordbank",
    "common",
    "instruments",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "django_admin_listfilter_dropdown",
    'ebhealthcheck.apps.EBHealthCheckConfig',
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

TEST_RUNNER = "django.test.runner.DiscoverRunner"

BLOGGER_API_KEY = os.environ["BLOGGER_API_KEY"]
BLOG_ID = os.environ["BLOG_ID"]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = os.environ["SENDGRID_KEY"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'