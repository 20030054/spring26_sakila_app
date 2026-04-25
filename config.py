# Name: Abdul Raffay Qasim
# Name: Team Member
# Date: 2026-04-23
# Minor improvement after PR review
# Added after review feedback

#Author:Urwah Taj
#Date: 2026-04-23
# Purpose: Database configuration for Sakila Flask Application

# Author: Team Member = Aliyah Cheema
# Date: 2026-04-23
# Purpose: Health check configuration merged from feature/add-healthcheck

# Author: Hassan Aslam - Date: 2026-04-25
# Purpose: Sets MySQL host and connection timeout configuration.
#Team Member = Hassan  Date: 2026-04-25
import os

class Config:
    MYSQL_HOST = "sakila-db-server"
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
    MYSQL_HOST = 'mysql-container'
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')


