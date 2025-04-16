"""
ASGI config for funtech project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import dotenv

from django.core.asgi import get_asgi_application

if os.path.isfile(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")):
    dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funtech.settings.' + os.environ.get("ENVIRONMENT"))

application = get_asgi_application()
