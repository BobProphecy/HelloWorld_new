from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from sales_view.udfs import *

def join_sales(
        spark: SparkSession,
        hello_world_hw_orders: DataFrame,
        hello_world_hw_customers: DataFrame,
) -> DataFrame:
    return hello_world_hw_orders\
        .alias("hello_world_hw_orders")\
        .join(
          hello_world_hw_customers.alias("hello_world_hw_customers"),
          (col("hello_world_hw_orders.customer_id") == col("hello_world_hw_customers.customer_id")),
          "inner"
        )\
        .select(col("hello_world_hw_orders.customer_id").alias("customer_id"), col("hello_world_hw_orders.order_id").alias("order_id"), col("hello_world_hw_customers.first_name").alias("first_name"), col("hello_world_hw_customers.last_name").alias("last_name"), col("hello_world_hw_orders.amount").alias("amount"), col("hello_world_hw_customers.email").alias("email"))
