#!/bin/bash

RELATIVE_PATH="$(dirname $0)/../"
ROOT_PATH="$(readlink -f $RELATIVE_PATH)"
PIDFILE="${ROOT_PATH}/django-flup.pid"

git pull --ff-only

find . -iname '*.pyc' -exec rm {} \;

kill `cat $PIDFILE`
sudo service nginx reload