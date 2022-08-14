# Python Import:
import os

# Django import:
from django.core.asgi import get_asgi_application

# Channels Import:
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Application Import:
from messages.notifications.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autocli.settings')
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
})
