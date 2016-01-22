from .base import *  # noqa


DEBUG = False

INSTALLED_APPS += (
    'gunicorn',
)

ALLOWED_HOSTS = ['127.0.0.1', ]

try:  # import the local settings
    from .private import *  # noqa
except ImportError:
    print('No tiene definidas configuraciones privadas')
