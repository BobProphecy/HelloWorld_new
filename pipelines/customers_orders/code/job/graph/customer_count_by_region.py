from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def customer_count_by_region(spark: SparkSession, apply_region_business_rule: DataFrame) -> DataFrame:
    df1 = apply_region_business_rule.groupBy(col("region"))

    return df1.agg(count(lit(1)).alias("CUSTOMER_COUNT"))
