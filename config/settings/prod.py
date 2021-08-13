from .base import *

ALLOWED_HOSTS = ['3.38.84.114', 'e-plate.co.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
# ---------------------------------- [edit] ---------------------------------- #
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': 'ahnse0512#',
        'HOST': 'ls-af6a858f9e519c300628cf64837cc9bbd782f0aa.cudjjnwh8xnw.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
# ---------------------------------------------------------------------------- #