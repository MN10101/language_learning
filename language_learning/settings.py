import os
from pathlib import Path
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent


# Secret Key Configuration
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', '*****************)')

# Debug Mode
DEBUG = True

# Allowed Hosts Configuration
ALLOWED_HOSTS = [
    's8m-adaptable-hubble.circumeo-apps.net',
    'localhost',
    '127.0.0.1',
]

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://s8m-adaptable-hubble.circumeo-apps.net',
    'http://localhost',
    'http://127.0.0.1',
]

# Application Definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'learning',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'learning.middleware.DisableCacheMiddleware',
]


ROOT_URLCONF = 'language_learning.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'learning/templates')],  
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

WSGI_APPLICATION = 'language_learning.wsgi.application'

# Database Configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'language_learning_db',
#         'USER': 'postgres',
#         'PASSWORD': '****',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Time Zone and Internationalization
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Debug Mode Check
DEBUG = True  


# Default Primary Key Field Type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Use ManifestStaticFilesStorage for cache busting
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Login and Authentication
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'welcome'
LOGOUT_REDIRECT_URL = 'login'

# Session Management

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Security settings for the session cookie
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = not DEBUG  
SESSION_COOKIE_HTTPONLY = True  


# CSRF Cookie Settings
CSRF_COOKIE_HTTPONLY = True  
CSRF_COOKIE_SAMESITE = 'Lax'  
CSRF_COOKIE_SECURE = not DEBUG  

# Security Settings (Enable in production)
SECURE_SSL_REDIRECT = not DEBUG  
SECURE_HSTS_SECONDS = 3600  
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'j.education.system@gmail.com'
EMAIL_HOST_PASSWORD = '***********'
DEFAULT_FROM_EMAIL = 'j.education.system@gmail.com'

# Stripe Configuration
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '****')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '****')

# Site ID (for Django's Sites Framework)
SITE_ID = 1
