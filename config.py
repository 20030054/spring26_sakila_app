# Author: Hania
# Date: 2026-04-27
# Description: Config with Config class for app import

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

class Config:
    MYSQL_HOST = MYSQL_HOST
    MYSQL_USER = MYSQL_USER
    MYSQL_PASSWORD = MYSQL_PASSWORD
    MYSQL_DB = MYSQL_DB
    CONNECTION_TIMEOUT = CONNECTION_TIMEOUT
    HEALTH_CHECK_INTERVAL = HEALTH_CHECK_INTERVAL
