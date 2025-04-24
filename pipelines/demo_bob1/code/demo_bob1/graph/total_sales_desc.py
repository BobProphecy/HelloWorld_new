from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def total_sales_desc(spark: SparkSession, customer_sales_summary: DataFrame) -> DataFrame:
    return customer_sales_summary.orderBy(col("TOTAL_SALES").desc())
