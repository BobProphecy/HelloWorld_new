from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def total_sales_by_customer(spark: SparkSession, sales_summary_by_customer: DataFrame) -> DataFrame:
    return sales_summary_by_customer.select(
        col("full_name"), 
        round(col("SUM_sales_amount"), 2).alias("TOTAL_SALES"), 
        col("ORDER_COUNT")
    )
