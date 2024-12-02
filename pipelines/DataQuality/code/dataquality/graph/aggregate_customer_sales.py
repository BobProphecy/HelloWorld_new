from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataquality.config.ConfigStore import *
from dataquality.functions import *

def aggregate_customer_sales(spark: SparkSession, clean_up: DataFrame) -> DataFrame:
    df1 = clean_up.groupBy(
        col("CUSTOMER_ID"), 
        col("FULL_NAME"), 
        col("PHONE"), 
        col("EMAIL"), 
        col("EMAIL_DOMAIN"), 
        col("COUNTRY_CODE")
    )

    return df1.agg(count(col("ORDER_ID")).alias("order_count"), sum(col("AMOUNT")).alias("sales_total"))
