# ============================================================
# config.py
# Team Member: ALI HASSAN
# Date: 2026-04-21
# Notes: Added health check interval configuration
# ============================================================
import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'db-primary')
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))


MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')