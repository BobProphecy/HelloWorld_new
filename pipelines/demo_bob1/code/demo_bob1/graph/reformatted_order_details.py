from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def reformatted_order_details(spark: SparkSession, order_customer_details: DataFrame) -> DataFrame:
    return order_customer_details.select(
        col("customer_id"), 
        concat(col("first_name"), lit(" "), col("last_name")).alias("full_name"), 
        col("order_id"), 
        col("amount").alias("sales_amount"), 
        substring_index(col("email"), "@", -1).alias("company_name")
    )
