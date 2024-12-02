from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def ProphecyAPI(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .option("multiLine", True)\
        .schema(
          StructType([
            StructField("info", StructType([
              StructField("_exporter_id", StringType(), True), StructField("_postman_id", StringType(), True), StructField("description", StringType(), True), StructField("name", StringType(), True), StructField("schema", StringType(), True)
            ]), True), StructField("item", ArrayType(
            StructType([
              StructField("item", ArrayType(
              StructType([
                StructField("name", StringType(), True), StructField("request", StructType([
                  StructField("body", StructType([
                    StructField("graphql", StructType([
                      StructField("query", StringType(), True), StructField("variables", StringType(), True)
                    ]), True), StructField("mode", StringType(), True)
                  ]), True), StructField("header", ArrayType(StringType(), True), True), StructField("method", StringType(), True), StructField("url", StructType([
                    StructField("host", ArrayType(StringType(), True), True), StructField("raw", StringType(), True)
                  ]), True)
                ]), True), StructField("response", ArrayType(StringType(), True), True)
            ]), 
              True
            ), True), StructField("name", StringType(), True)
          ]), 
            True
          ), True), StructField("variable", ArrayType(
            StructType([
              StructField("key", StringType(), True), StructField("type", StringType(), True), StructField("value", StringType(), True)
          ]), 
            True
          ), True)
        ])
        )\
        .load("dbfs:/FileStore/bobwelshmer/sample_data/ProphecyAPI_GraphQL.json")
