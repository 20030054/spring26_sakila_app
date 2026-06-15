import os

# updated by Rana Tashfeen Fazal
# updated by Rana Tashfeen Fazal (team member)

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'password')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

# Validation for HEALTH_CHECK_INTERVAL
if HEALTH_CHECK_INTERVAL <= 0:
    HEALTH_CHECK_INTERVAL = 10
