# Author: Wania Masood
# Date: 2026-04-23
# Purpose: Update database config

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))