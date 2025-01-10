from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def total_sales_by_customer(spark: SparkSession, customer_order_summary: DataFrame) -> DataFrame:
    return customer_order_summary.select(
        col("full_name"), 
        round(col("SUM_AMOUNT"), 2).alias("TOTAL_SALES"), 
        col("ORDER_COUNT")
    )
