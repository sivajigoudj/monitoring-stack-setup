from datetime import datetime, timedelta
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.stats import Stats
from airflow.models.pool import Pool
from airflow.settings import Session

def push_pool_metrics():
    session = Session()

    pools = session.query(Pool).all()
    for pool in pools:
        used = pool.running_slots(session=session)
        total = pool.slots

        # Send to StatsD → statsd-exporter → Prometheus
        Stats.gauge(f"pool_{pool.pool}_used", used)
        Stats.gauge(f"pool_{pool.pool}_total", total)

    session.close()

with DAG(
    dag_id="airflow_pool_metrics",
    schedule_interval="*/1 * * * *",  # every 1 min
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    push_metrics = PythonOperator(
        task_id="push_pool_metrics",
        python_callable=push_pool_metrics
    )

