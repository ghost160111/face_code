#!/bin/bash
set -e

echo "Ensuring pip is installed/upgraded..."
py -m ensurepip --upgrade || echo "ensurepip failed"
py -m pip install --upgrade pip

echo "Installing requirements..."
py -m pip install -r requirements.txt

echo "Collecting static files..."
py manage.py collectstatic --noinput

echo "Making migrations..."
python3.9 manage.py makemigrations

echo "Applying migrations..."
py manage.py migrate

echo "Creating superuser (non-interactively)..."
py manage.py shell -c "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
admin_username = 'admin'; admin_email = 'admin@example.com'; admin_password = 'your_secret_password'; \
if not User.objects.filter(username=admin_username).exists(): \
    User.objects.create_superuser(admin_username, admin_email, admin_password); \
else: \
    print('Superuser already exists')"
