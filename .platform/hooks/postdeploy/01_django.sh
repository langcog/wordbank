#!/bin/bash

source "$PYTHONPATH/activate" && {
# specify the management commands you want to run here

python ./manage.py migrate --noinput;
python ./manage.py createsu;
python ./manage.py collectstatic --noinput;
python ./manage.py aggregate_stats;
}