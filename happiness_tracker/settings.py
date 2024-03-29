# https://docs.djangoproject.com/en/4.0/ref/settings/

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import django_on_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()  # take environment variables from .env.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") in ["True", "true", "1"]
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") in ["True", "true", "1"]
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

print(' >>> DEBUG:', DEBUG)

######################################################  Application definition

INSTALLED_APPS = [
    'tracker.apps.TrackerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'static_precompiler'
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

ROOT_URLCONF = 'happiness_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'happiness_tracker.wsgi.application'


###################################################### Login

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

###################################################### Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASE_URL = os.getenv("DATABASE_URL", "False") in ["True", "true", "1"]
if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=True),
    }

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


######################################################  Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


###################################################### Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True


######################################################  Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'tracker/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'tracker/static/')
STATICFILES_DIRS = []
STATIC_PRECOMPILER_COMPILERS = (
    'static_precompiler.compilers.SCSS',
)
STATIC_PRECOMPILER_OUTPUT_DIR = os.path.join(BASE_DIR, 'tracker/static/')

STATIC_PRECOMPILER_COMPILERS = (
    ('static_precompiler.compilers.libsass.SCSS', { "output_style": "compact" }),
)


###################################################### Deploy

if DEVELOPMENT_MODE is False:
    # Configure Django App for Heroku.
    django_on_heroku.settings(locals())
    del DATABASES['default']['OPTIONS']['sslmode']
