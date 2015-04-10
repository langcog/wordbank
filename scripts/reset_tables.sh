#!/bin/sh

echo "Deleting old tables..."
./manage.py delete_all_tables

echo "Populating Instruments..."
./manage.py populate_instrumentsmap

echo "Populating Category..."
./manage.py populate_category

echo "Populating Word Mapping..."
./manage.py populate_word_mapping

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
