#!/bin/bash


find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate


python manage.py loaddata "Companies.json"
python manage.py loaddata "JobsVacancies.json"
python manage.py loaddata "WebUser.json"
python manage.py loaddata "WebUserAdm.json"
python manage.py loaddata "WebUserCompany.json"
python manage.py loaddata "JobsApplications.json"

./populate.sh

# python manage.py loaddata "MerchantJoao.json"
