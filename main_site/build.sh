#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create a superuser (replace 'admin', 'admin@example.com', and 'adminpass' with your desired username, email, and password)
python manage.py shell <<EOF
from django.contrib.auth.models import User
User.objects.create_superuser('jayanth', 'chjayanth119@gmail.com', 'HAKUNAmatata1@')
EOF
