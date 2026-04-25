# Name: Rafay Azim
# Date: 2026-04-24
# Purpose: Add health check interval (feature/add-healthcheck)

import os

class Config:
    """Base configuration class for Sakila Flask application"""
    
    MYSQL_HOST = 'db-primary'
    
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
