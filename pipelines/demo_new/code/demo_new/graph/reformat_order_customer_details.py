from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def reformat_order_customer_details(spark: SparkSession, order_customer_details: DataFrame) -> DataFrame:
    return order_customer_details.select(
        concat(col("FIRST_NAME"), lit(" "), col("LAST_NAME")).alias("full_name"), 
        col("AMOUNT"), 
        col("ORDER_ID")
    )
