# Name: Sara Mir & Team Member X
# Date: 2026-04-26
# Purpose: Merged configuration updates from both branches

import os

class Config:
    """Base configuration class for Sakila Flask application"""
    
    MYSQL_HOST = 'sakila-db-server'
    
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))