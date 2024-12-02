from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dataquality.config.ConfigStore import *
from dataquality.functions import *
from prophecy.utils import *
from dataquality.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_customers = customers(spark)
    df_join_customers_orders = join_customers_orders(spark, df_customers, df_orders)
    df_DQ_orders_out0, df_DQ_orders_out1 = DQ_orders(spark, df_orders)
    df_clean_up = clean_up(spark, df_join_customers_orders)
    df_DQ_customer_out0, df_DQ_customer_out1 = DQ_customer(spark, df_customers)
    df_aggregate_customer_sales = aggregate_customer_sales(spark, df_clean_up)
    df_by_sales_total_desc = by_sales_total_desc(spark, df_aggregate_customer_sales)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("DataQuality")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/DataQuality")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/DataQuality", config = Config)(pipeline)

if __name__ == "__main__":
    main()
