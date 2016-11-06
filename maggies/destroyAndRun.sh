#!/bin/bash
clear
echo "Installing requirements"
pip install -r requirements.txt
rm -r -f db.sqlite3

echo ""
echo "Migrating db"
python manage.py migrate --run-syncdb   # don't create superuser

echo ""
echo "About to populate"
python populate.py  # run population script to add admin

echo ""
echo "The server is about to run..."
echo "3, 2, 1..."

python manage.py runserver
