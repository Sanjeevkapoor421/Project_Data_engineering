import kaggle
import os
import pandas as pd
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

# Function to download data from kaggle via api call

os.environ['KAGGLE_CONFIG_DIR'] = '/home/airflow/.config/kaggle'

#Kaggle API authentication

def Fetch_kaggle_data(dataset_name,output_path):
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, path = output_path, unzip = True)
    print(f"Dataset fetched and unzipped successfully to {output_path}")

def upload_to_snowflake(table_name, input_csv_path):

    hook = SnowflakeHook(snowflake_conn_id='snowflake_conn') 
    conn = hook.get_conn()
    df = pd.read_csv(input_csv_path)
    cursor = conn.cursor()
   
    qualified_table_name = 'DBT_DB.staging.' + table_name
    
    # Create table if it does not exist
    columns_ddl = ', '.join([f'"{col}" VARCHAR' for col in df.columns])
    create_table_query = f'CREATE OR REPLACE TABLE {qualified_table_name} ({columns_ddl})'
    cursor.execute(create_table_query)


    temp_csv_file = '/tmp/temp_upload.csv'
    df.to_csv(temp_csv_file, index=False)

    # 3. Upload to Snowflake stage
    cursor.execute("CREATE OR REPLACE TEMPORARY STAGE my_stage;")
    cursor.execute(f"""
        PUT file://{temp_csv_file}
        @my_stage
        AUTO_COMPRESS=TRUE
    """)

    # 4. Copy into table
    cursor.execute(f"""
        COPY INTO {qualified_table_name}
        FROM @my_stage
        FILE_FORMAT = (TYPE='CSV' FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1);
    """)

    cursor.close()
    print(f"Data uploaded to Snowflake table {table_name} successfully.")
    conn.close()
