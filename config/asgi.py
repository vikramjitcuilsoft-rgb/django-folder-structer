import os
from pathlib import Path
from dotenv import load_dotenv

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.routing import websocket_urlpatterns

# Load .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

env = os.getenv("DJANGO_ENV", "local")
print(f"🔧 Loading Django settings: config.settings.{env}")

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    f"config.settings.{env}"
)

# Initialize Django
django_asgi_app = get_asgi_application()

# ✅ Log DB after Django setup
from common.db_logger import log_database_info
log_database_info()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
