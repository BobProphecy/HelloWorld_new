from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def CC_TranX(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .option("mode", "DROPMALFORMED")\
        .schema(
          StructType([
            StructField("_corrupt_record", StringType(), False), StructField("card_holder_id", StringType(), True), StructField("card_number", StringType(), True), StructField("card_type", StringType(), True), StructField("merchant_address", StringType(), True), StructField("merchant_category", StringType(), True), StructField("merchant_city", StringType(), True), StructField("merchant_country", StringType(), True), StructField("merchant_name", StringType(), True), StructField("merchant_postal_code", StringType(), True), StructField("merchant_state", StringType(), True), StructField("transaction_amount", DoubleType(), True), StructField("transaction_datetime", StringType(), True), StructField("transaction_id", LongType(), True), StructField("transaction_seatlement_date", StringType(), True)
        ])
        )\
        .load("dbfs:/FileStore/bobwelshmer/sample_data/transaction.json")
