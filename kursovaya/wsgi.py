"""
WSGI config for kursovaya project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kursovaya.settings')

application = get_wsgi_application()