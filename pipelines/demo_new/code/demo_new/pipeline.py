from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_new.config.ConfigStore import *
from demo_new.functions import *
from prophecy.utils import *
from demo_new.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_orders = collectMetrics(spark, df_orders, "graph", "HoGifkeL", "xFOYXoAD")
    df_customers = customers(spark)
    df_customers = collectMetrics(spark, df_customers, "graph", "E42HttKO", "YOs7o1AY")
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_order_customer_details = collectMetrics(spark, df_order_customer_details, "graph", "nQlwtHPh", "zRrID8GW")
    df_reformat_order_customer_details = reformat_order_customer_details(spark, df_order_customer_details)
    df_reformat_order_customer_details = collectMetrics(
        spark, 
        df_reformat_order_customer_details, 
        "graph", 
        "QkLI6rDd-XsOpVvNa9PO0$$b10g-cBYM3oetnukUKu_g", 
        "yU26tKC7cdu0sIPRlyQh-$$6nLwd3Cb4pPvy_lzfcrnl"
    )
    df_customer_order_summary = customer_order_summary(spark, df_reformat_order_customer_details)
    df_customer_order_summary = collectMetrics(spark, df_customer_order_summary, "graph", "peqqsGoe", "hWN2GFjE")
    df_total_sales_by_customer = total_sales_by_customer(spark, df_customer_order_summary)
    df_total_sales_by_customer = collectMetrics(spark, df_total_sales_by_customer, "graph", "GBlkBHRy", "czsUgjY6")
    df_sorted_total_sales = sorted_total_sales(spark, df_total_sales_by_customer)
    df_sorted_total_sales = collectMetrics(spark, df_sorted_total_sales, "graph", "gxdNwzk3", "On3ysPLA")
    df_limited_sort_results = limited_sort_results(spark, df_sorted_total_sales)
    df_limited_sort_results = collectMetrics(spark, df_limited_sort_results, "graph", "tTzZKbzD", "paMRpUv0")
    demo_rt(spark, df_limited_sort_results)

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
