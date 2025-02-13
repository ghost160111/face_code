"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``app``.
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = get_wsgi_application()

# Ensure migrations are applied on each cold start
try:
    call_command("migrate", "--noinput")
    print("✅ Migrations applied successfully.")
except Exception as e:
    print(f"❌ Migration failed: {e}")

# Ensure superuser is created only once
try:
    User = get_user_model()
    if not User.objects.filter(username="root").exists():
        User.objects.create_superuser("root", "admin@example.com", "1")
        print("✅ Superuser 'root' created successfully.")
    else:
        print("⚡ Superuser 'root' already exists, skipping creation.")
except Exception as e:
    print(f"❌ Superuser creation failed: {e}")
