from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def select_ranked_customers(spark: SparkSession, row_number_by_customer_count: DataFrame) -> DataFrame:
    return row_number_by_customer_count.select(col("row_count"), col("region"), col("CUSTOMER_COUNT"))
