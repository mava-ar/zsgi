from .base import *  # noqa

DEBUG = False

INSTALLED_APPS += (
    'gunicorn',
)

ALLOWED_HOSTS = ['127.0.0.1', ]