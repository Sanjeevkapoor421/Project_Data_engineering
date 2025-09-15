from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="dbt_forecasting",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["forecasting"]
) as dag:

    run_dbt_reporting = BashOperator(
        task_id="run_dbt_reporting",
        bash_command="cd /opt/airflow/dags/sanjeev_dbt && dbt run --select category_city_metrics"
    )
