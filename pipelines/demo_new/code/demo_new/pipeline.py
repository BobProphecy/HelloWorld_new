from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from demo_new.config.ConfigStore import *
from demo_new.functions import *
from prophecy.utils import *
from demo_new.graph import *

def pipeline(spark: SparkSession) -> None:
    df_orders = orders(spark)
    df_orders = collectMetrics(spark, df_orders, "graph", "TZIEqsEn", "M34WizN3")
    df_customers = customers(spark)
    df_customers = collectMetrics(spark, df_customers, "graph", "CdZPwkHp", "zPkfO0Xy")
    df_order_customer_details = order_customer_details(spark, df_orders, df_customers)
    df_order_customer_details = collectMetrics(spark, df_order_customer_details, "graph", "ZfsRguwE", "ZPO8w2Om")
    df_reformat_order_customer_details = reformat_order_customer_details(spark, df_order_customer_details)
    df_reformat_order_customer_details = collectMetrics(
        spark, 
        df_reformat_order_customer_details, 
        "graph", 
        "IRbuJrnB-ffalXyy0bfDz$$s_SgdkB_DDfqyt4Apu1u3", 
        "gT89dZGw0xGTrBE6e1Ng_$$Rchpy-38A_j2olMlSgBqe"
    )
    df_sales_summary_by_customer = sales_summary_by_customer(spark, df_reformat_order_customer_details)
    df_sales_summary_by_customer = collectMetrics(spark, df_sales_summary_by_customer, "graph", "RMYbaBFI", "GHH7gt8q")
    df_total_sales_by_customer = total_sales_by_customer(spark, df_sales_summary_by_customer)
    df_total_sales_by_customer = collectMetrics(spark, df_total_sales_by_customer, "graph", "jcAURqpE", "yPygtHHi")
    df_total_sales_desc = total_sales_desc(spark, df_total_sales_by_customer)
    df_total_sales_desc = collectMetrics(spark, df_total_sales_desc, "graph", "mkZ3VRCE", "mPUd1ePo")
    df_limited_sort_results = limited_sort_results(spark, df_total_sales_desc)
    df_limited_sort_results = collectMetrics(spark, df_limited_sort_results, "graph", "pECrxbH0", "vGXGYzIR")
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
