"""
WSGI config for cellcycle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(root_path)
sys.path.insert(0, root_path)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
