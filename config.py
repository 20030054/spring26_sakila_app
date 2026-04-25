# Author: M. Saad Asim
# Date: April 25, 2026

import os

MYSQL_HOST = 'db-primary'
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))