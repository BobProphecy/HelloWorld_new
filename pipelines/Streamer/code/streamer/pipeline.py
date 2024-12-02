from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from streamer.config.ConfigStore import *
from streamer.functions import *
from prophecy.utils import *
from streamer.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Watermark_1 = Watermark_1(spark)
    df_Reformat_1 = Reformat_1(spark, df_Watermark_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Streamer")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Streamer")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Streamer", config = Config)(pipeline)
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()

if __name__ == "__main__":
    main()
