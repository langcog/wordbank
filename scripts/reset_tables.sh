echo "Deleting old tables..."
./manage.py delete_all_tables
echo "Initializing all tables..."
./manage.py initialize_all_tables
echo "Populating Ethnicity..."
./manage.py populate_ethnicity
echo "Populating Source..."
./manage.py populate_source
echo "Populating CDI Category..."
./manage.py populate_cdi_category "raw_data/ws_categories.xlsx"
./manage.py populate_cdi_category "raw_data/wg_categories.xlsx"
echo "Importing Norming WS..."
./manage.py import_ws "raw_data/CDI-WS-2.xlsx"
echo "Importing WS Dallas..."
./manage.py import_ws "raw_data/MarchmanDallas.xlsx"
echo "Importing WS Wisconsin..."
./manage.py import_ws "raw_data/MarchmanWisconsin.xlsx"
echo "Importing WS Indiana..."
./manage.py import_ws "raw_data/LindaSmith.xlsx"
./manage.py import_ws "raw_data/LindaSmithQualtrics.xlsx"
echo "Importing WG..."
./manage.py import_wg "raw_data/CDI-WG-2.xlsx"
echo "Aggregating Stats..."
./manage.py aggregate_stats
echo "Done."
