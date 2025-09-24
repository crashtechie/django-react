"""
ASGI config for customer_management project.
"""

import os

from django.core.asgi import get_asgi_application  # type: ignore

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "customer_management.settings")

application = get_asgi_application()
