#!/usr/bin/env bash
# Exit on error
set -o errexit

# Poetry installation (if you're using Poetry)
# curl -sSL https://install.python-poetry.org | python3 -

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate

# Create superuser if needed (optional)
# if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] && [ "$DJANGO_SUPERUSER_EMAIL" ]; then
#     python manage.py createsuperuser --noinput
# fi