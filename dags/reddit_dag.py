from airflow import DAG
from datetime import datetime
import os
import sys

from airflow.operators.python import PythonOperator
from sqlalchemy import extract

from pipelines.reddit_pipeline import reddit_pipeline

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Mamadou BA',
    'start_date': datetime(2024, 10, 21)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag  = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit','etl','pipeline']
)

################################### 1. Extraction from reddit #################################################

extract = PythonOperator(
    task_id='reddit_extract',
    python_callable=reddit_pipeline,
    op_kwargs= {
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    }
)


################################### 2. Upload to S3 ###########################################################
