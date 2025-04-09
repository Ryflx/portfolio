#!/bin/bash
# Exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create a static directory if it doesn't exist
mkdir -p static

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate 