# Name: Rafay Azim
# Name: Rafay Azim
# Date: 2026-04-24
# Purpose: Combined config after merge conflict resolution

import os

class Config:
    """Base configuration class for Sakila Flask application"""
    
    MYSQL_HOST = 'sakila-db-server'
    
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))