from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define the default_args dictionary to specify the default parameters of the DAG
default_args = {
    "depends_on_past": False,
    'owner': 'airflow',
    'start_date': datetime(2023, 12, 16),
    'email_on_failure': False,
}

# Create a DAG instance
dag = DAG(
    'weather_etl',
    default_args=default_args,
    description='Weather ETL Pipeline to run every 15 minutes',
    schedule_interval='*/15 * * * *'
)

def print_begin():
    print("Begin ETL process")

def run_python_script():
    # Import your Python script here
    exec(open("/Users/poojasingh/Documents/Git_Reposit/DataEnggProjects/Weather_ETL/etl_script.py").read())

def print_end():
    print("ETL process completed")


with dag:
    print_begin_task = PythonOperator(
        task_id='print_begin_task',
        python_callable=print_begin,
        dag=dag,
    )

    execute_etl_task = PythonOperator(
        task_id='execute_etl_task',
        python_callable=run_python_script,
        dag=dag,
    )

    print_end_task = PythonOperator(
        task_id='print_end_task',
        python_callable=print_end,
        dag=dag,
    )

    print_begin_task >> execute_etl_task >> print_end_task


