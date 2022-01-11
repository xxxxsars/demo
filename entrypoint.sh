#!/bin/bash
set -e

echo "${0}: running migrations."
python /demo/manage.py makemigrations --merge
python /demo/manage.py migrate --noinput

#echo "${0}: collecting statics."
#python manage.py collectstatic --noinput

echo "${0}: running server."
python /demo/manage.py runserver 0.0.0.0:8000
