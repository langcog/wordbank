#echo "Creating instrument schemas..."
#./manage.py create_instrument_schemas

echo "Deleting old tables..."
./manage.py delete_all_tables

echo "Initializing new tables..."
./manage.py initialize_all_tables

echo "Populating Word Mapping..."
./manage.py populate_word_mapping

echo "Populating Source..."
./manage.py populate_source

while read dataset; do
    s=${dataset}
    s=${s##*/}
    s=${s%.*}
    echo "Importing $s...";
    ./manage.py import_data $dataset
done < raw_data/datasets.txt
#while read instrument; do
#    for dataset in datasets; do
#    for data_file in raw_data/${instrument}/*; do
#        s=${data_file}
#        s=${s##*/}
#        s=${s%.*}
#        if [[ $s != '['*']' ]] && [[ $s != '~'* ]]; then
#            echo "Importing $s..."
#                ./manage.py import_data ${data_file}
#        fi
#    done
#done < raw_data/instruments.txt

echo "Aggregating Stats..."
./manage.py aggregate_stats

echo "Done."