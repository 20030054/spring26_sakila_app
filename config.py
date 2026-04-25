# config.py
# Author: M. Asham Khan | Date: 2026-04-25
# Author: Abdul Rafay Asad | Date: 2026-04-25
# Description: Updated DB host, added timeout and health check settings

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
