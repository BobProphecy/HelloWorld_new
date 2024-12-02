from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def TestJSON(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .schema(
          StructType([
            StructField("address", StringType(), True), StructField("age_group", DoubleType(), True), StructField("creation_date", StringType(), True), StructField("email", StringType(), True), StructField("firstname", StringType(), True), StructField("gender", DoubleType(), True), StructField("id", LongType(), True), StructField("lastname", StringType(), True)
        ])
        )\
        .load("dbfs:/Users/nathan@prophecy.io/demos/retail/auto_loader/user_json/")
