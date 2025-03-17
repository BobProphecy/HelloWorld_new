from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from schemachange.config.ConfigStore import *
from schemachange.functions import *

def stooges3(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("employee_id", StringType(), True), StructField("f_name", StringType(), True), StructField("l_name", StringType(), True), StructField("title", StringType(), True), StructField("manager_id", StringType(), True), StructField("test_flag", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/stooges.csv")
