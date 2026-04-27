# Configuration updates
# Author: Shaheer Nawaz
# Team Member: Simulated Team Member
# Date: 2026-04-25
# Purpose: Resolved database host conflict and kept timeout plus health
# check settings.

import os


MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

try:
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
except ValueError:
    CONNECTION_TIMEOUT = 30

try:
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
except ValueError:
    HEALTH_CHECK_INTERVAL = 10


class Config:
    """Base configuration class for the Sakila Flask application."""

    MYSQL_HOST = MYSQL_HOST
    MYSQL_USER = MYSQL_USER
    MYSQL_PASSWORD = MYSQL_PASSWORD
    MYSQL_DB = MYSQL_DB
    CONNECTION_TIMEOUT = CONNECTION_TIMEOUT
    HEALTH_CHECK_INTERVAL = HEALTH_CHECK_INTERVAL
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'your-secret-key-here-change-this-in-production'
    )
