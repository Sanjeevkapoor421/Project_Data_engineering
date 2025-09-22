# Project_Data_engineering
A end-to-end ETL pipeline that will be fetching data from Kaggle via api, Ingest into snowflake, Transform the raw table into Fact and Dimension Table via DBT, Aggregated a table for reporting, and visualizes trends in Looker Studio.

# Tech Stacks
* Sowflake for storage/compute
* DBT for SQL transformation 
* Apache Airflow for orchestraction(Docker)
* Looker Studio for dashboard

# Note:Prerequisite
 * Install Docker in your system and make sure its running in background.
 * Create a api key from kaggle and download it in json format.
 * Create a snowflake trail accound and fetch the details like Account, User, Passowrd, Role, Data warehouse, Database and Schema.
 * Create a foler Credentials in this director and add the file kaggle.json and your snowflake credentials as .env file
 * Add your snowflake credentials to the profiles.yml in the folder sanjeev_dbt under dags folder.

# 🚀Run this project:

### 1) Clone this project to your local using the below git command 
    ```bash
    git clone https://github.com/Sanjeevkapoor421/Project_Data_engineering.git
    cd Project_Data_engineering
    ```
### 2) Do git checkout to developement_branch
    ```bash
    git checkout features/base
    ```
### 3) Setting up the virtual environment and running the project
    ```bash
    make all
    ``` 
This will :
 * create a virtual environment " myenv " ✅
 * It will install the required dependencies from requirements file ✅
 * Lastly it will run the Docker container file ✅
 * Triggers the Pipeline that will fetch the kaggle and ingest to snowflake✅

# 🛠️ Manually run this project if the above ' make ' command didn't work
    ```bash
    python3.12 -m venv myenv
    source myenv/bin/activate
    pip install -r requirements.txt
    Docker-compose up --build -d 
    ```
# 🛠️ Manually check the status in Airflow UI for the ingestion, transformation and logs.
 * The airflow will be pointing to your localhost. Go to http://localhost:8080/ in your browser
 * Use the credentials given in the entrypoint.sh file to login.
 * Trigger the pipeline to do individual transformations and to check logs.
