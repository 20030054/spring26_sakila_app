# Improved configuration after PR review feedback
# Update by Ramsha - update-config branch
# Update by Team Member - healthcheck branch - 2026-04-26

import os


class Config:
    """Base configuration class for the Sakila Flask application.
    Handles database connection strings and system timeouts.
    """

    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')

    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'your-secret-key-here-change-this-in-production'
    )