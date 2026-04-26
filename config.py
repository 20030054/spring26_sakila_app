# Name: M Zakriya Ahmed
# Date: 2026-04-26
# Purpose: Configuration for Sakila App with Timeout and Health Check

import os

MYSQL_HOST = 'db-primary'
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

# End of configuration
