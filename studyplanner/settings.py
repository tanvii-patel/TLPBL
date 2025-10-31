"""
Django settings for studyplanner project.
"""

from pathlib import Path
from django.utils import timezone

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------
# SECURITY
# ------------------------------------------------------------
SECRET_KEY = 'django-insecure-1+0(0zh6ss+2h3wihkva3_jfez!yxzz9)(wojehyp&w(5mfzeo'
DEBUG = True
ALLOWED_HOSTS = []

# ------------------------------------------------------------
# APPLICATION DEFINITION
# ------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # your main app
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

ROOT_URLCONF = 'studyplanner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'studyplanner.wsgi.application'

# ------------------------------------------------------------
# DATABASE
# ------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------------------------------------
# PASSWORD VALIDATION
# ------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ------------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # set to Indian Standard Time
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------
# STATIC & MEDIA FILES
# ------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------------------------------------------
# LOGIN & LOGOUT SETTINGS
# ------------------------------------------------------------
LOGIN_URL = '/login/'               # ✅ Fixes your 404 error
LOGIN_REDIRECT_URL = 'dashboard'         # after successful login
LOGOUT_REDIRECT_URL = 'home'        # after logout

# ------------------------------------------------------------
# DEFAULT PRIMARY KEY
# ------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
