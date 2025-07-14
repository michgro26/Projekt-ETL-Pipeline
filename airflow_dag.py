from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import etl_real_estate

def run_etl():
    exec(open("etl_real_estate.py").read())

dag = DAG(
    'real_estate_etl_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@monthly',
    catchup=False
)

run_etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag
)
