from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs import *
from prophecy.utils import *
from job.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_load_customers_dataset = load_customers_dataset(spark)
    df_select_customer_id = select_customer_id(spark, df_orders)
    df_distinct_customer_ids = distinct_customer_ids(spark, df_select_customer_id)
    df_join_by_customer_id = join_by_customer_id(spark, df_orders, df_load_customers_dataset)
    df_customer_data_cleanup = customer_data_cleanup(spark, df_join_by_customer_id)
    df_aggregate_sales_by_customer = aggregate_sales_by_customer(spark, df_customer_data_cleanup)
    df_by_sales_total_desc = by_sales_total_desc(spark, df_aggregate_sales_by_customer)
    save_us_sales_analysis(spark, df_by_sales_total_desc)
    write_customers_orders_csv(spark, df_by_sales_total_desc)
    df_apply_region_business_rule = apply_region_business_rule(spark, df_load_customers_dataset)
    df_customer_count_by_region = customer_count_by_region(spark, df_apply_region_business_rule)
    df_row_number_by_customer_count = row_number_by_customer_count(spark, df_customer_count_by_region)
    df_select_ranked_customers = select_ranked_customers(spark, df_row_number_by_customer_count)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/customers_orders")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/customers_orders", config = Config)(pipeline)

if __name__ == "__main__":
    main()
