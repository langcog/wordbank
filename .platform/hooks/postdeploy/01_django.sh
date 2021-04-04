#!/bin/bash

source "$PYTHONPATH/activate" && {
# migrate
if [[ $EB_IS_COMMAND_LEADER == "true" ]];
then
    python ./manage.py migrate --noinput;
    python ./manage.py createsu;
else
    echo "this instance is NOT the leader"
fi
}

python ./manage.py collectstatic --noinput;