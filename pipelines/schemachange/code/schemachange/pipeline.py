from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from schemachange.config.ConfigStore import *
from schemachange.functions import *
from prophecy.utils import *
from schemachange.graph import *

def pipeline(spark: SparkSession) -> None:
    df_stooges3 = stooges3(spark)
    df_employee_details_selection = employee_details_selection(spark, df_stooges3)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("schemachange").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/schemachange")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/schemachange", config = Config)(pipeline)

if __name__ == "__main__":
    main()
