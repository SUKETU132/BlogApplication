#!/bin/bash

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Start Django server (for testing purposes; Vercel will handle routing)
python3 manage.py runserver
