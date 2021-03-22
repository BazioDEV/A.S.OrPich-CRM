import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_main.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conduit.settings.development')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conduit.settings.production')

application = get_wsgi_application()
