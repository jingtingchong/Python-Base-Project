#!/bin/bash
# This script launches gunicorn WSGI
gunicorn service_provider.api.main:app \
         --workers $NUM_GUNICORN_WORKERS \
         --worker-class uvicorn.workers.UvicornWorker \
         --worker-tmp-dir /dev/shm \
         --bind 0.0.0.0:8000 \
         --timeout 0