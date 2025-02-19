from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def sorted_total_sales(spark: SparkSession, total_sales_by_customer: DataFrame) -> DataFrame:
    return total_sales_by_customer.orderBy(col("TOTAL_SALES").desc())
