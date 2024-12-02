from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testjson.config.ConfigStore import *
from testjson.udfs import *
from prophecy.utils import *
from testjson.graph import *

def pipeline(spark: SparkSession) -> None:
    df_CC_TranX = CC_TranX(spark)
    df_cc_transaction_reformat = cc_transaction_reformat(spark, df_CC_TranX)
    df_ProphecyAPI = ProphecyAPI(spark)
    df_flatten_api_schema = flatten_api_schema(spark, df_ProphecyAPI)
    prophecy_api_uc(spark, df_flatten_api_schema)
    df_TestJSON = TestJSON(spark)
    df_old_events_JSON = old_events_JSON(spark)
    df_flatten_schema = flatten_schema(spark, df_old_events_JSON)
    df_events_description_by_category2 = events_description_by_category2(spark, df_flatten_schema)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("TestJSON")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/TestJSON")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/TestJSON", config = Config)(pipeline)

if __name__ == "__main__":
    main()
