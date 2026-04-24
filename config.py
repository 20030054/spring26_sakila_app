# Name: Abeeha
# Date: 2026-04-24

import os

MYSQL_HOST = 'sakila-db-server'

CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))