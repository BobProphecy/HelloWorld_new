from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def customer_sales_summary(spark: SparkSession, sales_summary_by_customer_company: DataFrame) -> DataFrame:
    return sales_summary_by_customer_company.select(
        col("full_name"), 
        col("company_name"), 
        round(col("SUM_SALES_AMOUNT"), 2).alias("TOTAL_SALES"), 
        col("ORDER_COUNT")
    )
