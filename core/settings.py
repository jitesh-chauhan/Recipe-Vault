"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!r=hw#2(t!wuhrz=79o(5e5$iutu^glvswt3(-@z9#c!e7adu2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# SECURE_SSL_REDIRECT = True
# # SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# HSTS settings
# SECURE_HSTS_SECONDS=31536000
# SECURE_HSTS_PRELOAD=True
# SECURE_HSTS_INCLUDE_SUBDOMAINS=True


# SSL_CERTIFICATE = 'C:/Users/VaRdaiN/Desktop/Django/key'
# SSL_KEY = 'C:/Users/VaRdaiN/Desktop/Django/key'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    
   
]
EXTERNAL_APPS=[
    
    'vege',
]

INSTALLED_APPS+=EXTERNAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg4',
#         'NAME': 'Recipe Vault', 
#         'USER': 'postgres',
#         'PASSWORD': 'VardaiN1',
#         'HOST': '.vercel.app', 
#         'PORT': '8888',
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'django_postgres',
#         'PASSWORD': 'VardaiN',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }
# mongodb+srv://jitesh_chauhan:<password>@cluster0.zmfm3x2.mongodb.net/
# mongodb+srv://jitesh_chauhan:VardaiN@cluster0.zmfm3x2.mongodb.net/
# mongodb+srv://jitesh_chauhan:<password>@cluster0.zmfm3x2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
           "name": "VardaiN_db",
           "host":  "mongodb+srv://jitesh_chauhan:VardaiN@cluster0.zmfm3x2.mongodb.net/",
           "username": "jitesh_chauhan",
           "password": "VardaiN",
           "authMechanism": "SCRAM-SHA-1",
        }, 
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get("postgres"),
#         'USER': os.environ.get("django_postgres"),
#         'PASSWORD': os.environ.get("VardaiN"),
#         'HOST': os.environ.get("localhost"),
#         'PORT': os.environ.get("5432"),
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_root')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'staticfiles_build'),
]

# MEDIA_ROOT = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS=(
        os.path.join(BASE_DIR,'static','staticfiles_build'),
)


 
# STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# cloud image storage
# CLOUDINARY_URL = "cloudinary://234342994428838:dkEe10im2aa1oZSQeSVXwlTlFic@dj95lfmej"
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dj95lfmej',
    'API_KEY': '234342994428838',
    'API_SECRET': 'dkEe10im2aa1oZSQeSVXwlTlFic'
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
MEDIA_URLS ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
