#!/bin/sh

echo "Reseting database..."
mysql < scripts/reset_wordbank.txt

echo "Re-generating instrument schemas..."
rm instruments/models.py*
rm instruments/schemas/*
touch instruments/schemas/__init__.py
./manage.py create_instrument_schemas

echo "Re-making migrations..."
rm instruments/migrations/*
./manage.py makemigrations instruments
./manage.py makemigrations

echo "Migrating..."
./manage.py migrate

echo "Alterting some fields to UTF-8..."
mysql wordbank < scripts/alter_fields.txt

echo "Reseting tables..."
./scripts/reset_tables.sh