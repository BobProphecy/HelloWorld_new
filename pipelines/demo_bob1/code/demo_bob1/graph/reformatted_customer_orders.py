from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def reformatted_customer_orders(spark: SparkSession, order_customer_details: DataFrame) -> DataFrame:
    return order_customer_details.select(
        col("CUSTOMER_ID"), 
        concat(col("FIRST_NAME"), lit(" "), col("LAST_NAME")).alias("full_name"), 
        col("ORDER_ID"), 
        col("AMOUNT").alias("SALES_AMOUNT"), 
        substring_index(substring_index(col("EMAIL"), "@", -1), ".", 1).alias("company_name")
    )
