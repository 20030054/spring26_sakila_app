# Author: M. Abdullah Abbas | Date: 2026-04-26
# Teammate: Abdul Raffay Qasim | Date: 2026-04-26

import os
"""
Configuration settings for the Sakila Database connection.
"""

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'default-key-for-dev')

    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))