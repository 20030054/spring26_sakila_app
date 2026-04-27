# ============================================
# Authors: Abdul Raffay Qasim, Aliyah Cheema
# Date: 2026-04-23
# Purpose: Configuration for Sakila Flask Application
# ============================================
"""Configuration class for Sakila Flask Application."""

import os

class Config:
    MYSQL_HOST = 'sakila-db-server'  # chosen from first branch

    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
