#!/bin/bash
# entrypoint.sh

# Initialize the DB (safe to rerun)
airflow db migrate

# Create the admin user if it doesn't exist
airflow users create \
    --username sanjeev \
    --firstname sanjeevkapoor \
    --lastname sankaran \
    --role Admin \
    --email sanjeevkapoor421@gmail.com \
    --password kapoor1234 || true

# Run the main container command (webserver/scheduler/...)
exec "$@"