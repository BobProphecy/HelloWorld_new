from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataquality.config.ConfigStore import *
from dataquality.functions import *

def clean_up(spark: SparkSession, join_customers_orders: DataFrame) -> DataFrame:
    return join_customers_orders.select(
        col("CUSTOMER_ID"), 
        concat(col("FIRST_NAME"), lit(" "), col("LAST_NAME")).alias("FULL_NAME"), 
        col("PHONE"), 
        col("EMAIL"), 
        substring_index(col("EMAIL"), "@", -1).alias("EMAIL_DOMAIN"), 
        col("COUNTRY_CODE"), 
        col("ORDER_ID"), 
        col("AMOUNT")
    )
