#!/bin/bash

# Move into the working directory where our app code sits
cd /code

# Set fallback environment configurations
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

# Fire up Gunicorn. Since PATH points to the .venv, it will find it instantly!
exec gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app