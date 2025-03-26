from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def customer_data_cleanup(spark: SparkSession, By_CustomerId: DataFrame) -> DataFrame:
    return By_CustomerId.select(
        col("customer_id"), 
        concat(col("first_name"), lit(" "), col("last_name")).alias("full_name"), 
        col("order_id"), 
        col("amount"), 
        hash(col("customer_id")).alias("hash_customer_id"), 
        hash(col("order_id")).alias("hash_order_id"), 
        substring_index(col("email"), "@", -1).alias("company_name")
    )
