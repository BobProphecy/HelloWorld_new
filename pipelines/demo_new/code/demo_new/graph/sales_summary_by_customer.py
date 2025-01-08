from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def sales_summary_by_customer(spark: SparkSession, reformat_order_customer_details: DataFrame) -> DataFrame:
    df1 = reformat_order_customer_details.groupBy(col("full_name"))

    return df1.agg(sum(col("sales_amount")).alias("SUM_sales_amount"), count(col("order_id")).alias("ORDER_COUNT"))
