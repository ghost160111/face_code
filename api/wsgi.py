"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``app``.
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = get_wsgi_application()

# Ensure migrations are applied on each cold start
try:
    call_command("migrate", "--noinput")
    print("✅ Migrations applied successfully.")
except Exception as e:
    print(f"❌ Migration failed: {e}")
