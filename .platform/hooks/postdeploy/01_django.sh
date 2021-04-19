#!/bin/bash

source "$PYTHONPATH/activate" && {
# specify the management commands you want to run here

python ./manage.py migrate --noinput;
python ./manage.py createsu;
python ./manage.py collectstatic --noinput;
python ./manage.py delete_all_tables
python ./manage.py populate_instrument
python ./manage.py populate_category
python ./manage.py populate_items 
python ./manage.py populate_momed
python ./manage.py populate_source
python ./manage.py import_datasets -l 'American Sign Language'
python ./manage.py import_datasets -l 'English (Australian)'

}