# Team Member: TEAMMATE NAME | Date: 25-04-2026
# Update: Changed database host to primary and added health check interval

import os

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')  # DIFFERENT value
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))  # new
    