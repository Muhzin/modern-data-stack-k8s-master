from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_dbt():
    logger.info("Running dbt...")
    subprocess.run(['dbt', 'run'], check=True)
    logger.info("dbt run completed.")

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
        python_callable=lambda: logger.info("Ingesting data..."),
    )

    transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=run_dbt,
    )

    ingest_data >> transform_data
