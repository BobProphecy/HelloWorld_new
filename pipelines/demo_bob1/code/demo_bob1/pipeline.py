from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *
from prophecy.utils import *
from demo_bob1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_customers = customers(spark)
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_reformatted_order_details = reformatted_order_details(spark, df_order_customer_details)
    df_sales_summary_by_customer_company = sales_summary_by_customer_company(spark, df_reformatted_order_details)
    df_customer_sales_summary = customer_sales_summary(spark, df_sales_summary_by_customer_company)
    df_total_sales_desc = total_sales_desc(spark, df_customer_sales_summary)
    df_limited_sort_results = limited_sort_results(spark, df_total_sales_desc)
    demo_gart22(spark, df_limited_sort_results)

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
