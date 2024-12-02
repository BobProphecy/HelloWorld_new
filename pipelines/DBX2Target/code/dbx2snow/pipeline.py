from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from dbx2snow.config.ConfigStore import *
from dbx2snow.udfs import *
from prophecy.utils import *
from dbx2snow.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_orders = orders(spark)
    df_customers_orders_join = customers_orders_join(spark, df_customers, df_orders)
    df_revenue_by_customer = revenue_by_customer(spark, df_customers_orders_join)
    df_by_revenue_desc = by_revenue_desc(spark, df_revenue_by_customer)
    df_limit_50 = limit_50(spark, df_by_revenue_desc)
    tar_snow(spark, df_limit_50)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/DBX2Target")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/DBX2Target", config = Config)(pipeline)

if __name__ == "__main__":
    main()
