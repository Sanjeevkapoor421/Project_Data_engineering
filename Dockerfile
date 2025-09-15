FROM apache/airflow:2.8.2
USER airflow
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY credentials/ /opt/airflow/credentials/
COPY dags/ /opt/airflow/dags
COPY python_scripts/ /opt/airflow/python_scripts/
COPY output_kaggle_files/ /opt/airflow/output_kaggle_files/

ENV KAGGLE_CONFIG_DIR=/opt/airflow/credentials/kaggle
# CMD [ "python", "python_scripts/get_kaggle_data.py" ]

