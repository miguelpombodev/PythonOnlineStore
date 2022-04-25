#!/bin/bash

while ! pg_isready -q -h $PGHOST -p $PGPORT -U $PGUSER
do
  echo "$(date) - waiting for database to start"
  sleep 2
done

# Create database if it doesn't exist.
if [[ -z `psql -Atqc "\\list $PGDATABASE"` ]]; then
  echo "Database $PGDATABASE does not exist. Creating..."
  createdb -E UTF8 $PGDATABASE -l en_US.UTF-8 -T template0
  echo "Database $PGDATABASE created."
fi


# Create database if it doesn't exist.
if [[ -z `psql -Atqc "\\list $PGDATABASETEST"` ]]; then
  echo "Database $PGDATABASETEST does not exist. Creating..."
  createdb -E UTF8 $PGDATABASETEST -l en_US.UTF-8 -T template0
  echo "Database $PGDATABASETEST created."
fi

export FLASK_APP="manage.py"
export FLASK_DEBUG=1

if [ ! -d "migrations" ]; then

  echo "Initializing Migrations - Creating Migrations Folder"
  flask db init

fi

echo "Generating Migrations"
flask db migrate

echo "Applying Migrations to Database"
flask db upgrade


flask run -h 0.0.0.0 -p 5000