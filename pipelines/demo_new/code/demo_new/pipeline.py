from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_new.config.ConfigStore import *
from demo_new.functions import *
from prophecy.utils import *
from demo_new.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_customers = collectMetrics(spark, df_customers, "graph", "vsDt6wgy", "qmtr5qRR")
    df_orders = orders(spark)
    df_orders = collectMetrics(spark, df_orders, "graph", "NEj6dUrs", "xMIfMSuQ")
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_order_customer_details = collectMetrics(spark, df_order_customer_details, "graph", "p7yyhRNO", "NZPnMOaC")
    df_reformat_order_customer_details = reformat_order_customer_details(spark, df_order_customer_details)
    df_reformat_order_customer_details = collectMetrics(
        spark, 
        df_reformat_order_customer_details, 
        "graph", 
        "6kdoSTkWmkd9I4i_gzXQO$$iSoj-BqPq_wF9ql1vKNAX", 
        "W93fl9tytMgeniUEPR14q$$nFOzo_DEGCT9Ak3Mln13n"
    )
    df_customer_order_summary = customer_order_summary(spark, df_reformat_order_customer_details)
    df_customer_order_summary = collectMetrics(spark, df_customer_order_summary, "graph", "Xz6s4Nbi", "bR6xvPgn")
    df_total_sales_by_customer = total_sales_by_customer(spark, df_customer_order_summary)
    df_total_sales_by_customer = collectMetrics(spark, df_total_sales_by_customer, "graph", "MTEfuWZJ", "VLHqyn4s")
    df_total_sales_desc = total_sales_desc(spark, df_total_sales_by_customer)
    df_total_sales_desc = collectMetrics(spark, df_total_sales_desc, "graph", "tcixPnQ5", "AzwD35y6")
    df_Script_1 = Script_1(spark, df_reformat_order_customer_details)
    df_Script_1 = collectMetrics(
        spark, 
        df_Script_1, 
        "graph", 
        "SDzms38V9n1Zym4JNE406$$hsjIGSdI3TioxogbDz3-5", 
        "G8UloGnulMf4hK49K3Bye$$3s9PJ6C2-5IXM3bQG8AOR"
    )
    df_Script_1.cache().count()
    df_Script_1.unpersist()
    df_limited_sort_results = limited_sort_results(spark, df_total_sales_desc)
    df_limited_sort_results = collectMetrics(spark, df_limited_sort_results, "graph", "RAQRO9iP", "EKccezZj")
    df_limited_sort_results.cache().count()
    df_limited_sort_results.unpersist()

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
