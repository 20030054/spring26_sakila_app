# Configuration Header: Manahil Fatima - 2026-04-28
# Collaborative Update: Integrated health checks and connection timeouts

import os

# Database Configuration
# Requirement: keep MYSQL_HOST as 'sakila-db-server'
MYSQL_HOST = 'sakila-db-server'

# New Variables (Requirement: Include BOTH)
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

# Other settings...
DEBUG = True
