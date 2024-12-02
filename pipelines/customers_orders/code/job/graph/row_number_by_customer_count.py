from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def row_number_by_customer_count(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn("row_count", row_number().over(Window.partitionBy().orderBy(col("CUSTOMER_COUNT").desc())))
