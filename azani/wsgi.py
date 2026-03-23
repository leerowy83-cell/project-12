import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azani.settings')

# 'application' is the standard Django WSGI entry point
application = get_wsgi_application()

# 'app' alias — Render's default gunicorn command uses 'app:app'
# so this prevents a crash if someone forgets to set the start command
app = application
