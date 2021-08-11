#!/usr/bin/env bash

set -e

until pg_isready --host="${POSTGRES_HOST}" --username="${POSTGRES_USER}" --quiet; do
    sleep 1;
done

touch -a /squatofadt/log/uwsgi.log
touch -a /squatofadt/log/django.log

cd /squatofadt/src/website

./manage.py migrate --no-input

chown --recursive www-data:www-data /squatofadt/

echo "Starting uwsgi server."
uwsgi --chdir=/squatofadt/src/website \
    --module=squatofadt.wsgi:application \
    --master --pidfile=/tmp/project-master.pid \
    --socket=:8000 \
    --processes=5 \
    --uid=www-data --gid=www-data \
    --harakiri=20 \
    --post-buffering=16384 \
    --max-requests=5000 \
    --thunder-lock \
    --vacuum \
    --logfile-chown \
    --logto2=/squatofadt/log/uwsgi.log \
    --ignore-sigpipe \
    --ignore-write-errors \
    --disable-write-exception
