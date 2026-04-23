# Team Member: Ali Hassan
# Date: 2026-04-23
# Purpose: Add health check config

import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))