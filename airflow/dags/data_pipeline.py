from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def run_dbt():
    # dbt run logic
    pass

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 1),
}

with DAG(
    'data_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
) as dag:
    run_dbt = PythonOperator(
        task_id='run_dbt',
        python_callable=run_dbt,
    )
