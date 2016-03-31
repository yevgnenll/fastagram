from .partials import *


DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
    'raven.contrib.django.raven_compat',
]
