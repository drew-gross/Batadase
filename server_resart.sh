#!/bin/bash

ROOT_PATH="~/"

PIDFILE="${ROOT_PATH}/django-flup.pid"
OUTLOG="${ROOT_PATH}/django.out"
ERRLOG="${ROOT_PATH}/django.err"

git pull --ff-only

find . -iname '*.pyc' -exec rm {} \;

kill `cat $PIDFILE`

./Batadase/manage.py runfcgi pidfile=$PIDFILE debug=True outlog=$OUTLOG errlog=$ERRLOG

sudo service nginx reload