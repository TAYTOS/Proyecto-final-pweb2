#!/bin/bash

DJANGODIR=$(cd $(dirname $0)/.. && pwd)
DJANGO_SETTINGS_MODULE=proyecto_prueba.settings

cd $DJANGODIR/Proyecto-final-pweb2

source $DJANGODIR/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

exec python manage.py runserver 0:8000
