from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def old_events_JSON(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .option("multiLine", True)\
        .schema(
          StructType([
            StructField("result", StructType([
              StructField("count", StringType(), True), StructField("events", ArrayType(
              StructType([
                StructField("category1", StringType(), True), StructField("category2", StringType(), True), StructField("date", StringType(), True), StructField("description", StringType(), True), StructField("granularity", StringType(), True), StructField("lang", StringType(), True)
            ]), 
              True
          ), True)
            ]), True)
        ])
        )\
        .load("dbfs:/FileStore/bobwelshmer/sample_data/old_events_data.json")
