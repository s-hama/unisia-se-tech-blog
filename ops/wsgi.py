"""
WSGI config for ops project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
#!/var/www/vops/bin/python

import os
import logging
from django.core.wsgi import get_wsgi_application
import sys

sys.path.append(r'/var/www/vops/ops')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ops.settings")

application = get_wsgi_application()
logging.getLogger('command').debug('ON wsgi.py')
