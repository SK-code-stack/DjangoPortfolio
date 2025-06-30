#!/bin/bash

# Collect static files into the "staticfiles" directory
echo "Collecting static files..."
python3 manage.py collectstatic --noinput