from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_new.config.ConfigStore import *
from demo_new.functions import *

@instrument
def limited_sort_results(spark: SparkSession, total_sales_ordered: DataFrame) -> DataFrame:
    return total_sales_ordered.limit(25)
