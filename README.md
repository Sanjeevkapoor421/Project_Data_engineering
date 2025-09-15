# Project_Data_engineering
This Project is developed for my university assignment purpose

# Step1: create Virtual env
python3 -m vene myenv
source myenv/bin/activate

# Step32: install dbt deps for offline dbt runs
dbt deps

# Step3: Start the docker containers
Docker compose up -d

# Access the local Host
localhost:8080

