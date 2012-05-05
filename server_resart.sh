#!/bin/bash

git pull --ff-only

find . -iname '*.pyc' -exec rm {} \;

sudo service nginx reload