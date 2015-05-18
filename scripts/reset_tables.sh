#!/bin/sh

echo "Deleting old tables..."
./manage.py delete_all_tables

echo "Populating Instrument..."
./manage.py populate_instrument

echo "Populating Category..."
./manage.py populate_category

echo "Populating ItemInfo and ItemMap..."
./manage.py populate_items

echo "Populating Source..."
./manage.py populate_source

echo "Populating MomEd..."
./manage.py populate_momed

echo "Importing data..."
./manage.py import_all_datasets

echo "Populating Vocabulary Size..."
./manage.py populate_vocabulary_size

echo "Aggregating Stats..."
./manage.py aggregate_stats

echo "Done."
