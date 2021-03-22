from .settings import *

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'baziovip$database1',
        'USER': 'baziovip',
        'PASSWORD': 'Ar4n8nad',
        'HOST': 'baziovip.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        
    }
}