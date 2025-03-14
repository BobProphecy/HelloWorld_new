from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def customers_distinct_customer_ids(
        spark: SparkSession,
        customers: DataFrame,
        distinct_customer_ids: DataFrame,
) -> DataFrame:
    return customers\
        .alias("customers")\
        .join(
          distinct_customer_ids.alias("distinct_customer_ids"),
          (col("customers.customer_id") == col("distinct_customer_ids.customer_id")),
          "inner"
        )\
        .select(col("customers.first_name").alias("first_name"), col("customers.last_name").alias("last_name"), col("customers.email").alias("email"), col("customers.phone").alias("phone"))
