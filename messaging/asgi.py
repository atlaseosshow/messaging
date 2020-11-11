"""
ASGI config for messaging project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

import chat.routing as cr

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging.settings')
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  "websocket": AuthMiddlewareStack(
          URLRouter(
              cr.websocket_urlpatterns
          )
      ),
  # Just HTTP for now. (We can add other protocols later.)
})
