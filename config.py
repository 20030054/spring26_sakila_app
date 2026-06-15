# Developer: Rana Tashfeen Fazal
# Task: Resolved integration conflict by maintaining unified production database host configuration
# Metrics: Preserved core application timeouts and system health metrics

import os

# Production cluster database routing target profile
MYSQL_HOST = 'sakila-db-server'

# Maximum allowed transaction latency threshold (seconds)
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))

# System status evaluation tracking frequency (seconds)
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
