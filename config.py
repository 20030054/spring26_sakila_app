# Configuration update
# Author: Shaheer Nawaz
# Date: 2026-04-25
# Purpose: Updated database host and added connection timeout.

import os


MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

try:
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
except ValueError:
    CONNECTION_TIMEOUT = 30


class Config:
    """Base configuration class for the Sakila Flask application."""

    MYSQL_HOST = MYSQL_HOST
    MYSQL_USER = MYSQL_USER
    MYSQL_PASSWORD = MYSQL_PASSWORD
    MYSQL_DB = MYSQL_DB
    CONNECTION_TIMEOUT = CONNECTION_TIMEOUT
    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'your-secret-key-here-change-this-in-production'
    )
