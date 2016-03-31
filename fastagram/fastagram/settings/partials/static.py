import os
from .base_setting import PROJECT_DIR


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'dist', 'media')

STATICFILES_DIRS = [
    # os.path.join(PROJECT_DIR, 'dist', 'static'),
]
