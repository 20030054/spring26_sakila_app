# Author: Wania Masood
# Date: 2026-04-23
# Team Member: Ali Hassan
# Date: 2026-04-23
# Purpose: Combined config update — DB host, timeout, health check

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
CONNECTION_TIMEOUT = max(1, int(os.environ.get('CONNECTION_TIMEOUT', '30')))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
