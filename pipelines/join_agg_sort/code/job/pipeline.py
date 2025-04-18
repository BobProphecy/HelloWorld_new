from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Customers = Customers(spark)
    df_Orders = Orders(spark)
    df_PerCustomer = PerCustomer(spark, df_Customers, df_Orders)
    df_TotalByCustomer = TotalByCustomer(spark, df_PerCustomer)
    df_Cleanup = Cleanup(spark, df_TotalByCustomer)
    df_SortBiggestOrders = SortBiggestOrders(spark, df_Cleanup)
    WriteReport(spark, df_SortBiggestOrders)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/join_agg_sort")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/join_agg_sort", config = Config)(pipeline)

if __name__ == "__main__":
    main()
