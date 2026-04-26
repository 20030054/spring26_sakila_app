# Name: M Zakriya Ahmed
# Date: 2026-04-26
# Purpose: Configuration for Sakila App with Timeout and Health Check

import os

class Config:
    # Basic Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ci-test-key'
    
    # Raw MySQL variables expected by your tests
    MYSQL_HOST = os.environ.get('MYSQL_HOST') or '127.0.0.1'
    MYSQL_USER = os.environ.get('MYSQL_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'admin'
    MYSQL_DB = os.environ.get('MYSQL_DB') or 'sakila'
    
    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:admin@127.0.0.1/sakila'
    SQLALCHEMY_TRACK_MODIFICATIONS = False