from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from sales_view.config.ConfigStore import *
from sales_view.udfs import *

def calculate_factorial(spark: SparkSession, sales_view_unity: DataFrame) -> DataFrame:
    return sales_view_unity.select(factorial(col("order_id")).alias("test2"))
