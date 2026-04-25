# Name: Sara Mir
# Date: 2026-04-26
# Purpose: Update config for database host and timeout setting (feature/update-config)

import os

class Config:
    """Base configuration class for Sakila Flask application"""
    
    MYSQL_HOST = 'sakila-db-server'
    
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))