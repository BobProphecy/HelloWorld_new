from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def order_customer_details(spark: SparkSession, orders: DataFrame, customers: DataFrame, ) -> DataFrame:
    return orders\
        .alias("orders")\
        .join(customers.alias("customers"), (col("orders.customer_id") == col("customers.customer_id")), "inner")\
        .select(col("orders.order_id").alias("ORDER_ID"), col("orders.customer_id").alias("CUSTOMER_ID"), col("orders.order_status").alias("ORDER_STATUS"), col("orders.order_category").alias("ORDER_CATEGORY"), col("orders.order_date").alias("ORDER_DATE"), col("orders.amount").alias("AMOUNT"), col("customers.first_name").alias("first_name"), col("customers.last_name").alias("last_name"), col("customers.phone").alias("phone"), col("customers.email").alias("email"), col("customers.country_code").alias("country_code"), col("customers.account_open_date").alias("account_open_date"), col("customers.account_flags").alias("account_flags"))
