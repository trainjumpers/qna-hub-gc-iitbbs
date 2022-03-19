#!/usr/bin/bash

if [ $# -eq 0 ]
    then
        cp .env.test .env
    else
        cp .env.$1 .env
fi

echo "Copied test profile to current profile"

python delete_and_create_tables.py
echo "Deleted and recreated all tables in the testdb"

echo "Running all tests"
pytest