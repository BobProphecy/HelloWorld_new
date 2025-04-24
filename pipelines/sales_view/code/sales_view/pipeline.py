from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sales_view.config.ConfigStore import *
from sales_view.udfs import *
from prophecy.utils import *
from sales_view.graph import *

def pipeline(spark: SparkSession) -> None:
    df_sales_view_raw = sales_view_raw(spark, Config.sales_view_raw)
    df_sales_view_unity = sales_view_unity(spark, Config.sales_view_unity)
    df_calculate_factorial = calculate_factorial(spark, df_sales_view_unity)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("sales_view")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/sales_view")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/sales_view", config = Config)(pipeline)

if __name__ == "__main__":
    main()
