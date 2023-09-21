from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess

def run_dbt():
    subprocess.run(['dbt', 'run'], check=True)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 1),
}

with DAG(
    'data_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
) as dag:
    ingest_data = PythonOperator(
        task_id='ingest_data',
        python_callable=lambda: print("Ingesting data..."),
    )

    transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=run_dbt,
    )

    ingest_data >> transform_data
