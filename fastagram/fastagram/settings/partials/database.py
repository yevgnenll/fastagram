import dj_database_url
import os


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# DATABASE_NAME = os.environ.get("DATABASE_NAME")
# DATABASE_USER = os.environ.get("DATABASE_USER")
# DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

DATABASES = {
    'default':  dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
    )
}
