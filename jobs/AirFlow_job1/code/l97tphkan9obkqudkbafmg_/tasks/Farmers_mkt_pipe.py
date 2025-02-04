from l97tphkan9obkqudkbafmg_.utils import *

@task_wrapper(task_id = "Farmers_mkt_pipe")
def Farmers_mkt_pipe(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "Farmers_mkt_pipe",
        json = {
          "task_key": "Farmers_mkt_pipe", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "12.2.x-scala2.12", 
            "runtime_engine": "STANDARD", 
            "num_workers": 0.0, 
            "data_security_mode": "SINGLE_USER", 
            "custom_tags": {"ResourceClass" : "SingleNode"}, 
            "spark_conf": {
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/AirFlow_job1", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "9631", 
              "spark.prophecy.tasks": "H4sIAAAAAAAAAKuuBQBDv6ajAgAAAA==", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.prophecy.metadata.user.id": "5088", 
              "spark.master": "local[*, 4]", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": "false", 
              "spark.databricks.isv.product": "prophecy", 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.databricks.cluster.profile": "singleNode", 
              "spark.prophecy.execution.service.url": "wss://app.prophecy.io/execution/eventws"
            }, 
            "aws_attributes": {
              "first_on_demand": 1.0, 
              "availability": "SPOT_WITH_FALLBACK", 
              "zone_id": "auto", 
              "spot_bid_price_percent": 100.0
            }, 
            "spark_env_vars": {"PYSPARK_PYTHON" : "/databricks/python3/bin/python3", "SPARK_VERSION" : "3.5"}, 
            "enable_elastic_disk": False
          }, 
          "python_wheel_task": {
            "package_name": "farmers_markets_irs", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-8.8.0"}},                          {"pypi" : {"package" : "prophecy-libs==1.9.33"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/farmers_markets_irs-1.0-py3-none-any.whl"
                         }]
        },
        databricks_conn_id = "",
    )
