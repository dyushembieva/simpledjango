from .settings import *

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'simpledjango',
       'USER': 'simpledjangouser',
       'PASSWORD': 'simpledjango123',
       'HOST': 'localhost',
       'PORT': '',
   }
}
