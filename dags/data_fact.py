from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from datetime import timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),   
}

with DAG(
    dag_id="dbt_fact_and_dim",
    default_args = default_args,
    description="A DAG to run dbt models for fact and dimension tables",
    schedule_interval=None,
    catchup=False,
    tags=["fact"]
) as dag:

    run_dbt_fact_dim = BashOperator(
        task_id="run_dbt_fact_and_dim",
        bash_command="cd /opt/airflow/dags/sanjeev_dbt && dbt run --select fact_reviews dim_organization dim_city dim_category"
    )
