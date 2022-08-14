# Python import:
import os

# Django import:
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autocli.settings')
application = get_wsgi_application()
