# build_files.sh
pip install -r requirements.txt

# Install dependencies
pip install -r requirements.txt

# Build static assets
python manage.py collectstatic --noinput

# Start the Django development server
python manage.py runserver 0.0.0.0:$PORT