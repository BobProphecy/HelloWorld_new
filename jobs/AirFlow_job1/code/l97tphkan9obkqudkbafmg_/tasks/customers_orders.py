from l97tphkan9obkqudkbafmg_.utils import *

@task_wrapper(task_id = "customers_orders")
def customers_orders(ti=None, params=None, **context):
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "customers_orders",
        json = {
          "task_key": "customers_orders", 
          "new_cluster": {
            "node_type_id": "i4i.large", 
            "spark_version": "14.3.x-scala2.12", 
            "runtime_engine": "STANDARD", 
            "num_workers": 0.0, 
            "data_security_mode": "SINGLE_USER", 
            "enable_local_disk_encryption": False, 
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
            "driver_node_type_id": "i4i.large", 
            "cluster_source": "API", 
            "aws_attributes": {
              "first_on_demand": 1.0, 
              "availability": "SPOT_WITH_FALLBACK", 
              "zone_id": "auto", 
              "spot_bid_price_percent": 100.0
            }, 
            "spark_env_vars": {"SPARK_VERSION" : "3.5"}, 
            "enable_elastic_disk": True
          }, 
          "python_wheel_task": {
            "package_name": "customers_orders", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.5.0-8.8.0"}},                          {"pypi" : {"package" : "prophecy-libs==1.9.33"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/saas/app/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/customers_orders-1.0-py3-none-any.whl"
                         }]
        },
        databricks_conn_id = "",
    )
