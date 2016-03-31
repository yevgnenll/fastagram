import os
import dj_database_url

from .base_setting import PROJECT_DIR


ALLOWED_HOSTS = []


# Application definition
LOGIN_URL = '/login/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'dist', 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'dist', 'media')

STATICFILES_DIRS = [
    # os.path.join(PROJECT_DIR, 'dist', 'static'),
]
# custome auth
AUTH_USER_MODEL = 'users.user'
