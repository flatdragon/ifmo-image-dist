#!/bin/bash
set -e

if [ "$APP_ENV" = 'production' ]; then
  echo "Running Production Server..."
  exec uwsgi \
    --http "$HOSTNAME":"$APP_PORT" --wsgi-file ./src/app.py --callable app \
    --stats "$HOSTNAME":"$APP_STATS_PORT" --stats-http \
    --log-socket "$HOSTNAME":"$APP_LOGGER_PORT"
else
  echo "Running Development Server..."
  cd src
  export FLASK_APP=app.py
  export FLASK_ENV="$APP_ENV"
  exec flask run --host "$HOSTNAME" --port "$APP_PORT"
fi
