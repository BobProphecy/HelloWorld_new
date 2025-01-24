from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def by_sales_total_desc(spark: SparkSession, Aggregate_by_customer: DataFrame) -> DataFrame:
    return Aggregate_by_customer.orderBy(col("sales_total").desc())
