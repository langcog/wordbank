#!/bin/bash

source "$PYTHONPATH/activate" && {
# specify the management commands you want to run here

python ./manage.py migrate --noinput;
#python ./manage.py createsu;
python ./manage.py collectstatic --noinput;
python ./manage.py 03_populate_instrument
python ./manage.py 04_populate_category 
python ./manage.py 05_populate_items -l 'French (French)' -f WG
python ./manage.py 05_populate_items -l 'French (French)' -f WS
python ./manage.py 05_populate_items -l 'Arabic (Saudi)' -f WG
python ./manage.py 05_populate_items -l 'Estonian' -f WS
python ./manage.py 05_populate_items -l 'Catalan' -f WS
python ./manage.py 05_populate_items -l 'Korean' -f WGComp
python ./manage.py 05_populate_items -l 'French (Quebecois)' -f WG
python ./manage.py 05_populate_items -l 'Finnish' -f WGProd
python ./manage.py 05_populate_items -l 'Finnish' -f WGProdShort
python ./manage.py 05_populate_items -l 'English (American)' -f WG
python ./manage.py 05_populate_items -l 'Finnish' -f WS
python ./manage.py 05_populate_items -l 'Arabic (Saudi)' -f WS
python ./manage.py 05_populate_items -l 'Arabic (Saudi)' -f WSOther

python ./manage.py 06_populate_datasets

python ./manage.py 07_import_datasets -a 'raw_data/French_French_WS/FrenchFrenchWS_Tsuji.csv'
python ./manage.py 07_import_datasets -a 'raw_data/French_French_WS/FrenchFrenchWS_TsujiLabvanced.csv'
python ./manage.py 07_import_datasets -a 'raw_data/French_French_WG/FrenchFrenchWG_Tsuji.csv'
python ./manage.py 07_import_datasets -a 'raw_data/Arabic_Saudi_WG/ArabicSaudiWG_Alroqi.csv'
python ./manage.py 07_import_datasets -a 'raw_data/Estonian_WS/EstonianWS_Urm.csv'
python ./manage.py 07_import_datasets -a 'raw_data/Catalan_WS/CatalanWS_Serrat.csv'
python ./manage.py 07_import_datasets -a 'raw_data/Korean_WS/KoreanWS_Chosun.csv'
python ./manage.py 07_import_datasets -a 'raw_data/Korean_WGComp/KoreanWGComp_Chosun.csv'
python ./manage.py 07_import_datasets -l Swedish -f WG
python ./manage.py 07_import_datasets -l German -f WS
python ./manage.py 07_import_datasets -o 'Byers Heinlein Bilingual'
#python ./manage.py 07_import_datasets -l Finnish -f WGProd
python ./manage.py 07_import_datasets -l Finnish -f WGProdShort
#python ./manage.py 07_import_datasets -l 'English (American)' -f WG
python ./manage.py 07_import_datasets -l Finnish -f WS
python ./manage.py 07_import_datasets -l 'Arabic (Saudi)' -f WG
python ./manage.py 07_import_datasets -l 'Arabic (Saudi)' -f WS
python ./manage.py 07_import_datasets -l 'Arabic (Saudi)' -f WSOther

python ./manage.py 08_populate_vocabulary_size -l 'French (French)' -f WS
python ./manage.py 08_populate_vocabulary_size -l 'French (French)' -f WG
python ./manage.py 08_populate_vocabulary_size -l 'Arabic (Saudi)' -f WG
python ./manage.py 08_populate_vocabulary_size -l 'Arabic (Saudi)' -f WS
python ./manage.py 08_populate_vocabulary_size -l 'Estonian' -f WS
python ./manage.py 08_populate_vocabulary_size -l 'Catalan' -f WS
python ./manage.py 08_populate_vocabulary_size -l 'Korean' -f WS
python ./manage.py 08_populate_vocabulary_size -l 'Korean' -f WGComp
python ./manage.py 08_populate_vocabulary_size -l Swedish -f WG
python ./manage.py 08_populate_vocabulary_size -l German -f WS
python ./manage.py 08_populate_vocabulary_size -l 'French (Quebecois)' -f WG
python ./manage.py 08_populate_vocabulary_size -l 'English (American)' -f WS
#python ./manage.py 08_populate_vocabulary_size -l 'English (American)' -f WG
#python ./manage.py 08_populate_vocabulary_size -l 'Finish' -f WGProd
python ./manage.py 08_populate_vocabulary_size -l 'Finish' -f WGProdShort
python ./manage.py 08_populate_vocabulary_size -l 'Finish' -f WS

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
