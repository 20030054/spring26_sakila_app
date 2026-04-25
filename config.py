"""
config.py
Author: Asham Khan | Date: 2026-04-25
Author: Teammate Name | Date: 2026-04-25
Description: Database configuration module. Handles MySQL connection
settings including host, timeout, and health check intervals.
"""
import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
