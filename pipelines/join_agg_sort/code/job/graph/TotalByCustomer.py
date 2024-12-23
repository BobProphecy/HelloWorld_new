from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

def TotalByCustomer(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("customer_id"))

    return df1.agg(
        first(col("first_name")).alias("first_name"), 
        first(col("last_name")).alias("last_name"), 
        sum(col("amount")).alias("amounts")
    )
