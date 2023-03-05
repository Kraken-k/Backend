"""
WSGI config for epsilon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')

application = get_wsgi_application()
"""

import os
import sys    
mysite = r'C:/xampp/htdocs/Backend'
if mysite not in sys.path:sys.path.insert(0,mysite)
mysite = r'C:/xampp/htdocs/Backend/Backend'
if mysite not in sys.path:sys.path.insert(0,mysite)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Backend.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


