#!/bin/bash



# python manage.py loaddata "MerchantJoao.json"
coverage run --source='.' manage.py test
coverage html
coverage report
coverage-badge -o coverage.svg -f