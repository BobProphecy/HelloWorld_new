from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def cc_transaction_reformat(spark: SparkSession, CC_TranX: DataFrame) -> DataFrame:
    return CC_TranX.select(
        col("_corrupt_record"), 
        col("card_holder_id"), 
        col("card_number"), 
        col("card_type"), 
        col("merchant_address"), 
        col("merchant_category"), 
        col("merchant_city"), 
        col("merchant_country"), 
        col("merchant_name"), 
        col("merchant_postal_code"), 
        col("merchant_state"), 
        col("transaction_amount"), 
        col("transaction_datetime"), 
        col("transaction_id"), 
        lit("").alias("isNew"), 
        col("transaction_seatlement_date")
    )
