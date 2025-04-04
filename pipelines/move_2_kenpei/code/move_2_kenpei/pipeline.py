from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from move_2_kenpei.config.ConfigStore import *
from move_2_kenpei.functions import *
from prophecy.utils import *
from move_2_kenpei.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_orders = orders(spark)
    c2k(spark, df_customers)
    o2k(spark, df_orders)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("move_2_kenpei").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/move_2_kenpei")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/move_2_kenpei", config = Config)(pipeline)

if __name__ == "__main__":
    main()
