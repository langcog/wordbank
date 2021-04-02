#!/bin/bash

source "$PYTHONPATH/activate" && {
# migrate
if [[ $EB_IS_COMMAND_LEADER == "true" ]];
then
    python ./src/manage.py migrate --noinput;
    python ./src/manage.py collectstatic --noinput;
    python ./src/manage.py createsu;
else
    echo "this instance is NOT the leader"
fi
}