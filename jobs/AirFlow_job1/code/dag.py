import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from l97tphkan9obkqudkbafmg_.tasks import Farmers_mkt_pipe, customers_orders, join_agg_sort
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "l97tPHKAn9OBkQUDKbAFMg_", 
    schedule_interval = "0 0 * * 1", 
    default_args = {
      "owner": "Prophecy", 
      "email": "bobw@prophecy.io", 
      "email_on_failure": True, 
      "ignore_first_depends_on_past": True, 
      "do_xcom_push": True, 
      "pool": "2AGL95yk"
    }, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 7, 1, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    Farmers_mkt_pipe_op = Farmers_mkt_pipe()
    join_agg_sort_op = join_agg_sort()
    customers_orders_op = customers_orders()
    [Farmers_mkt_pipe_op, join_agg_sort_op] >> customers_orders_op
