#!/bin/bash
set -e

echo "Ensuring pip is installed/upgraded..."
python3.9 -m ensurepip --upgrade || echo "ensurepip failed"
python3.9 -m pip install --upgrade pip

echo "Installing requirements..."
python3.9 -m pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput

echo "Making migrations..."
python3.9 manage.py makemigrations

echo "Applying migrations..."
python3.9 manage.py migrate

echo "Creating superuser (non-interactively)..."
python3.9 manage.py shell -c "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
admin_username = 'admin'; admin_email = 'admin@example.com'; admin_password = 'your_secret_password'; \
if not User.objects.filter(username=admin_username).exists(): \
    User.objects.create_superuser(admin_username, admin_email, admin_password); \
else: \
    print('Superuser already exists')"
