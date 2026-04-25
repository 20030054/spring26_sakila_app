# Author:Muhammad Areeb & M Qasim(Teammate)
# Date: April 25, 2026
import os
"""Configuration settings for the Sakila application."""

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))