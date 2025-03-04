from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def sales_summary_by_customer(spark: SparkSession, reformatted_order_details: DataFrame) -> DataFrame:
    df1 = reformatted_order_details.groupBy(col("full_name"), col("company_name"))

    return df1.agg(sum(col("SALES_AMOUNT")).alias("SUM_SALES_AMOUNT"), count(col("ORDER_ID")).alias("ORDER_COUNT"))
