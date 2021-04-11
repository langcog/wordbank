#!/bin/bash

source "$PYTHONPATH/activate" && {
# migrate

python ./manage.py migrate --noinput;
python ./manage.py createsu;
python ./manage.py collectstatic --noinput;

}