#!/usr/bin/bash

# Activate the virtual env
source venv/bin/activate

if [ $# -eq 0 ]
    then
        cp .env.test .env
    else
        cp .env.$1 .env
fi

echo "Copied the environment file"

# Run the app
echo "Starting the app"
uvicorn app.main:app --reload --port 8000