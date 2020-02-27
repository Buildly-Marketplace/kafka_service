#!/bin/bash

set -e

bash scripts/wait-for-it.sh $DATABASE_HOST $DATABASE_PORT

echo $(date -u) "- Migrating"
python manage.py migrate

echo $(date -u) "- Creating admin user"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

echo $(date -u) "- Running the server"
gunicorn kafka_config.wsgi --config kafka_config/gunicorn_conf.py
