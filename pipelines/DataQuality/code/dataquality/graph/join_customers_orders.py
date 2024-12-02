from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataquality.config.ConfigStore import *
from dataquality.functions import *

def join_customers_orders(spark: SparkSession, customers: DataFrame, orders: DataFrame, ) -> DataFrame:
    return customers\
        .alias("customers")\
        .join(orders.alias("orders"), (col("customers.customer_id") == col("orders.customer_id")), "inner")\
        .select(col("customers.customer_id").alias("CUSTOMER_ID"), col("customers.first_name").alias("FIRST_NAME"), col("customers.last_name").alias("LAST_NAME"), col("customers.phone").alias("PHONE"), col("customers.email").alias("EMAIL"), col("customers.country_code").alias("COUNTRY_CODE"), col("orders.order_id").alias("ORDER_ID"), col("orders.amount").alias("AMOUNT"))
