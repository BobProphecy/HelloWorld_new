from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *
from prophecy.utils import *
from demo_bob1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_orders = orders(spark)
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("demo_bob1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/demo_bob1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/demo_bob1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
