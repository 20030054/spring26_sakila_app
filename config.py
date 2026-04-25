# Author: Maaz Butt | Date: 25-04-2026
# Team Member: TEAMMATE NAME | Date: 25-04-2026
# Resolution: Kept sakila-db-server as host, included both new variables
# Fix: Added input validation for timeout variables after PR review

import os

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

    try:
        CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    except ValueError:
        CONNECTION_TIMEOUT = 30

    try:
        HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
    except ValueError:
        HEALTH_CHECK_INTERVAL = 10