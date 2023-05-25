#!/bin/bash
source /venv/bin/activate
exec gunicorn elitegooners.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3
````
chmod +x gunicorn_start.sh
````

