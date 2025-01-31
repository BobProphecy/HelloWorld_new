from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_new.config.ConfigStore import *
from demo_new.functions import *
from prophecy.utils import *
from demo_new.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_orders = collectMetrics(spark, df_orders, "graph", "AicMnLmZ", "BUts8k7X")
    df_customers = customers(spark)
    df_customers = collectMetrics(spark, df_customers, "graph", "MqjAFaW0", "Y1LBg8Nh")
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_order_customer_details = collectMetrics(spark, df_order_customer_details, "graph", "wHjw6FmA", "gohyDzYv")
    df_reformat_order_customer_details = reformat_order_customer_details(spark, df_order_customer_details)
    df_reformat_order_customer_details = collectMetrics(
        spark, 
        df_reformat_order_customer_details, 
        "graph", 
        "prDe9lEa2aC2KuJwVt0YS$$cUv41B7m0zdn4I3UOY5Uj", 
        "7OmnOScW05G5Jpy8S_TRT$$oTKiGOYW7I8fLhZcpK7aT"
    )
    df_reformat_order_customer_details.cache().count()
    df_reformat_order_customer_details.unpersist()

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("demo_new")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/demo_new")
    registerUDFs(spark)
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/demo_new", config = Config)(
        MetricsCollector.withSparkOptimisationsDisabled(pipeline)
    )

if __name__ == "__main__":
    main()
