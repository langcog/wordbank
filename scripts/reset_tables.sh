./manage.py delete_all_tables
./manage.py initialize_all_tables
./manage.py populate_ethnicity
./manage.py populate_source
./manage.py import_ws "raw_data/CDI-WS-2.xlsx"
./manage.py import_ws "raw_data/MarchmanDallas.xlsx"
./manage.py import_ws "raw_data/MarchmanWisconsin.xlsx"
./manage.py import_wg "raw_data/CDI-WG-2.xlsx"
./manage.py aggregate_stats
