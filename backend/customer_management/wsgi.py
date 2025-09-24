"""
WSGI config for customer_management project.
"""

import os

from django.core.wsgi import get_wsgi_application  # type: ignore

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "customer_management.settings")

application = get_wsgi_application()
