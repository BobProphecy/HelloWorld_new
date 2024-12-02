from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dbx2snow.config.ConfigStore import *
from dbx2snow.udfs import *

def revenue_by_customer(spark: SparkSession, customers_orders_join: DataFrame) -> DataFrame:
    df1 = customers_orders_join.groupBy(col("CUSTOMER_ID"), col("FIRST_NAME"), col("LAST_NAME"))

    return df1.agg(sum(col("amount")).alias("REVENUE"), count(col("order_id")).alias("order_count"))
