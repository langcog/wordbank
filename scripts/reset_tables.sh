echo "Deleting old tables..."
./manage.py delete_all_tables

echo "Initializing new tables..."
./manage.py initialize_all_tables

echo "Populating Word Mapping..."
./manage.py populate_word_mapping

echo "Populating Source..."
./manage.py populate_source

echo "Populating MomEd..."
./manage.py populate_momed

echo "Importing data..."
./manage.py import_all_datasets

echo "Aggregating Stats..."
./manage.py aggregate_stats

echo "Done."