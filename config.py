<<<<<<< HEAD
# Contributor: Fizza Mahmood
# Date: 2026-04-24
# Purpose: Combined configuration after resolving merge conflict

=======
>>>>>>> main
import os


class Config:
<<<<<<< HEAD
   """Configuration class for Sakila Flask application including database, timeout, and health check settings."""
=======
    """Base configuration class for the Sakila Flask application.
    Handles database connection strings and system timeouts.
    """
>>>>>>> main

    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

<<<<<<< HEAD
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')
=======
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')
>>>>>>> main
