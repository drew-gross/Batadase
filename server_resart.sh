#!/bin/bash

ROOT_PATH="~/"

PIDFILE="${ROOT_PATH}/django-flup.pid"
SOCKETFILE="${ROOT_PATH}/django.sock"
OUTLOG="${ROOT_PATH}/django.out"
ERRLOG="${ROOT_PATH}/django.err"

git pull --ff-only

find . -iname '*.pyc' -exec rm {} \;

kill `cat $PIDFILE`

sg croutonlabs_web "./manage.py runfcgi socket=$SOCKETFILE pidfile=$PIDFILE umask=0002 debug=True outlog=$OUTLOG errlog=$ERRLOG"

sudo service nginx reload