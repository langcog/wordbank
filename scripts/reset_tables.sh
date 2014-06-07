echo "Deleting old tables..."
./manage.py delete_all_tables
echo "Initializing all tables..."
./manage.py initialize_all_tables
echo "Populating Ethnicity..."
./manage.py populate_ethnicity
echo "Populating Source..."
./manage.py populate_source
echo "Importing Norming WS..."
./manage.py import_ws "raw_data/CDI-WS-2.xlsx"
echo "Importing Dallas..."
./manage.py import_ws "raw_data/MarchmanDallas.xlsx"
echo "Importing Wisconsin..."
./manage.py import_ws "raw_data/MarchmanWisconsin.xlsx"
echo "Importing WG..."
./manage.py import_wg "raw_data/CDI-WG-2.xlsx"
echo "Aggregating Stats..."
./manage.py aggregate_stats
echo "Done."
