<<<<<<< HEAD
# Author: Muhammad Qasim Tahir
=======
# Author: M. Saad Asim
>>>>>>> feature/add-healthcheck
# Date: April 25, 2026

import os

<<<<<<< HEAD
MYSQL_HOST = 'sakila-db-server'
CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
=======
MYSQL_HOST = 'db-primary'
HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))
>>>>>>> feature/add-healthcheck
