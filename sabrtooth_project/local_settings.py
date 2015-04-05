from settings import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sabr',
        'USER': 'iamdangeruss',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
