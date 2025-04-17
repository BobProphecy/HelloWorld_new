from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def order_customer_details(spark: SparkSession, orders: DataFrame, customers: DataFrame, ) -> DataFrame:
    return orders\
        .alias("orders")\
        .join(customers.alias("customers"), (col("orders.customer_id") == col("customers.customer_id")), "inner")\
        .select(col("orders.order_id").alias("ORDER_ID"), col("orders.customer_id").alias("CUSTOMER_ID"), col("orders.order_status").alias("ORDER_STATUS"), col("orders.order_category").alias("ORDER_CATEGORY"), col("orders.order_date").alias("ORDER_DATE"), col("orders.amount").alias("AMOUNT"), col("customers.first_name").alias("FIRST_NAME"), col("customers.last_name").alias("LAST_NAME"), col("customers.phone").alias("PHONE"), col("customers.email").alias("EMAIL"), col("customers.country_code").alias("COUNTRY_CODE"), col("customers.account_open_date").alias("ACCOUNT_OPEN_DATE"), col("customers.account_flags").alias("ACCOUNT_FLAGS"))
