from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_new.config.ConfigStore import *
from demo_new.functions import *
from prophecy.utils import *
from demo_new.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_customers = collectMetrics(spark, df_customers, "graph", "g2hZrAvf", "uGmP4fYm")
    df_orders = orders(spark)
    df_orders = collectMetrics(spark, df_orders, "graph", "GRMe7Mwr", "LCgxzi8k")
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_order_customer_details = collectMetrics(spark, df_order_customer_details, "graph", "wuGC07om", "lWHNGulu")
    df_reformat_order_customer_details = reformat_order_customer_details(spark, df_order_customer_details)
    df_reformat_order_customer_details = collectMetrics(
        spark, 
        df_reformat_order_customer_details, 
        "graph", 
        "MQz04ZsCMMmyo3hwOUUgG$$l438Eo9uC3nBp5yAyLEnd", 
        "rkf98-iyk6Q6YL7twK8UW$$lk6eFWbLjilEczqtrYL86"
    )
    df_sales_summary_by_customer = sales_summary_by_customer(spark, df_reformat_order_customer_details)
    df_sales_summary_by_customer = collectMetrics(spark, df_sales_summary_by_customer, "graph", "lza4XKiz", "RKCqIIeR")
    df_total_sales_by_customer = total_sales_by_customer(spark, df_sales_summary_by_customer)
    df_total_sales_by_customer = collectMetrics(spark, df_total_sales_by_customer, "graph", "MB6YZIKF", "dgu3tRHQ")
    df_total_sales_ordered = total_sales_ordered(spark, df_total_sales_by_customer)
    df_total_sales_ordered = collectMetrics(spark, df_total_sales_ordered, "graph", "AygDTQ22", "q7nUVzoG")
    df_limited_sort_results = limited_sort_results(spark, df_total_sales_ordered)
    df_limited_sort_results = collectMetrics(spark, df_limited_sort_results, "graph", "sllM14Dy", "DGIl5ght")
    demo_callum(spark, df_limited_sort_results)

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
