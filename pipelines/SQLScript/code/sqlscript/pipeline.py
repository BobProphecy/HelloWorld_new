from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sqlscript.config.ConfigStore import *
from sqlscript.udfs import *
from prophecy.utils import *
from sqlscript.graph import *

def pipeline(spark: SparkSession) -> None:
    df_customers = customers(spark)
    df_select_hw_customer = select_hw_customer(spark, df_customers)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("SQLScript")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SQLScript")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/SQLScript", config = Config)(pipeline)

if __name__ == "__main__":
    main()
