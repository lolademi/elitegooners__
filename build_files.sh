# build_files.sh

#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Build static assets
python3.11.0 manage.py collectstatic --noinput

# Run any necessary database migrations
python3.11.0 manage.py migrate

# Start the Django development server
python3.11.0 manage.py runserver 0.0.0.0:$PORT