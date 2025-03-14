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
        .select(col("orders.order_id").alias("order_id"), col("orders.customer_id").alias("customer_id"), col("orders.order_status").alias("order_status"), col("orders.order_category").alias("order_category"), col("orders.order_date").alias("order_date"), col("orders.amount").alias("amount"), col("customers.first_name").alias("first_name"), col("customers.last_name").alias("last_name"), col("customers.phone").alias("phone"), col("customers.email").alias("email"), col("customers.country_code").alias("country_code"), col("customers.account_open_date").alias("account_open_date"), col("customers.account_flags").alias("account_flags"))
