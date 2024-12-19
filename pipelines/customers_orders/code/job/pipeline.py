from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Orders = Orders(spark)
    df_Customers = Customers(spark)
    df_By_CustomerId = By_CustomerId(spark, df_Orders, df_Customers)
    df_clean_up = clean_up(spark, df_By_CustomerId)
    df_Aggregate_by_customer = Aggregate_by_customer(spark, df_clean_up)
    df_OrderBy_Sales = OrderBy_Sales(spark, df_Aggregate_by_customer)
    Unity(spark, df_OrderBy_Sales)
    CSV(spark, df_OrderBy_Sales)
    df_apply_region_business_rule = apply_region_business_rule(spark, df_Customers)
    df_customer_count_by_region = customer_count_by_region(spark, df_apply_region_business_rule)
    df_row_number_by_customer_count = row_number_by_customer_count(spark, df_customer_count_by_region)
    df_Ranked = Ranked(spark, df_row_number_by_customer_count)
    df_data_quality_checks_out0, df_data_quality_checks_out1 = data_quality_checks(spark, df_Orders)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customers_orders")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/customers_orders", config = Config)(pipeline)

if __name__ == "__main__":
    main()
