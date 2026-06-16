import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline
from utils.constants import REDDIT_POST_LIMIT, REDDIT_SUBREDDIT, REDDIT_TIME_FILTER

default_args = {
    'owner': 'Admin',
    'start_date': datetime(2023, 10, 22)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='personal_reddit_analytics_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'personal', 'analytics']
)

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': REDDIT_SUBREDDIT,
        'time_filter': REDDIT_TIME_FILTER,
        'limit': REDDIT_POST_LIMIT
    },
    dag=dag
)

# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3
