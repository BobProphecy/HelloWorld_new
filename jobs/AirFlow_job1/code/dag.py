import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from _xxvfkzggtsnckiazoarsg_.tasks import DBX2Target
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "_XXvFkZggTSnckIazoArSg_", 
    schedule_interval = "0 0 * * *", 
    default_args = {
      "owner": "Prophecy", 
      "email": "bobw@prophecy.io", 
      "email_on_failure": True, 
      "ignore_first_depends_on_past": True, 
      "do_xcom_push": True, 
      "pool": "_6YCC4gT"
    }, 
    start_date = pendulum.datetime(2025, 3, 24, tz = "UTC"), 
    end_date = pendulum.datetime(2025, 4, 13, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    DBX2Target_op = DBX2Target()
