from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '123123123'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "zilleprojects", # "zweb_test"
        'USER': "root",  # ,"root"
        'PASSWORD': "zille123",  # , "zille123"
        "HOST": "127.0.0.1",  # , "127.0.0.1"
        "POST": "3306"
    }
}

COMPRESS_ENABLED = False
