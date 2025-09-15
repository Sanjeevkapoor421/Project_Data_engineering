from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from datetime import timedelta
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'python_scripts'))
from get_kaggle_data import Fetch_kaggle_data, upload_to_snowflake

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),   
}

with DAG(  
    dag_id = 'dag_etl_pipeline',
    default_args = default_args,
    description = 'A DAG to load data from Kaggle and upload it to Snowflake',
    schedule_interval = None,
    catchup = False,
    tags = ['data_loading'],
) as dag: 
      
    fetch_task = PythonOperator(
        task_id = 'fetch_kaggle_data',
        python_callable = Fetch_kaggle_data,
        op_args = ['abdulmajid115/yelp-dataset-contains-1-million-rows', '/opt/airflow/output_kaggle_files/'],
    )
    load_task = PythonOperator(
        task_id='upload_to_snowflake',
        python_callable=upload_to_snowflake, 
        op_args=['yelp_raw_data','/opt/airflow/output_kaggle_files/yelp_database.csv'],
    )
    transform_task = BashOperator(
        task_id="run_dbt_fact_and_dim",
        bash_command="cd /opt/airflow/dags/sanjeev_dbt && dbt run --select fact_reviews dim_organization dim_city dim_category"
    )
    run_dbt_reporting = BashOperator(
        task_id="run_dbt_reporting",
        bash_command="cd /opt/airflow/dags/sanjeev_dbt && dbt run --select category_city_metrics"
    )

    fetch_task >> load_task >> transform_task >> run_dbt_reporting