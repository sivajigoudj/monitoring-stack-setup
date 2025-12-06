# dags/example_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('example_dag', start_date=datetime(2025,12,6), schedule_interval='@once', catchup=False) as dag:
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

