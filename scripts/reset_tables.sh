source env/bin/activate
./manage.py delete_all_tables
./manage.py initialize_all_tables
./manage.py import_ws
./manage.py import_wg
