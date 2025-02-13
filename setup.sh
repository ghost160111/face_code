#!/bin/bash
set -e

echo "Running migrations..."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate


echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser..."
python manage.py shell -c "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
admin_username = 'admin'; \
admin_email = ''; \
admin_password = 'facecode'; \
if not User.objects.filter(username=admin_username).exists(): \
    User.objects.create_superuser(admin_username, admin_email, admin_password); \
else: \
    print('Superuser already exists')"
