#!/bin/bash

source "$PYTHONPATH/activate" && {
# specify the management commands you want to run here

python ./manage.py migrate --noinput;
python ./manage.py createsu;
python ./manage.py collectstatic --noinput;

#clear down and set up basic database records
#python ./manage.py delete_all_tables
#python ./manage.py populate_instrument
#python ./manage.py populate_category
#python ./manage.py populate_items 
#python ./manage.py populate_caregiver_education
#python ./manage.py populate_source

#load a specific dataset
#python ./manage.py import_datasets -l 'English (Australian)'

}