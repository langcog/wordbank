if [ $# != 2 ]
	then
	echo "Provide a language and a form, for example by running"
	echo "./import_instrument.sh Wugese WS"
else
	./manage.py migrate
	./manage.py populate_instrumentsmap
	./manage.py populate_category
	./manage.py populate_word_mapping $1 $2
	./manage.py populate_source
	./manage.py import_instrument_datasets $1 $2
	./manage.py populate_vocabulary_size $1 $2
fi