# Name: M Zakriya Ahmed
# Date: 2026-04-26
# Purpose: Configuration for Sakila App with Timeout and Health Check

import os

class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ci-test-key'
    
    # Database connection string (defaults to local MySQL for CI testing)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:admin@127.0.0.1/sakila'
    
    # Disable modification tracking to save memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False