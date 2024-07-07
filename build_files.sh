#!/bin/bash

echo "BUILD START"

# Assuming Python 3.9 is your desired Python version
python3.9 -m pip install -r requirements.txt  # Install dependencies

python3.9 manage.py collectstatic --noinput --clear  # Collect static files

# Additional commands as needed for your build process

echo "BUILD END"
