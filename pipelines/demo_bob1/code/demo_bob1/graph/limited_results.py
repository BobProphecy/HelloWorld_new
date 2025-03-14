from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from demo_bob1.config.ConfigStore import *
from demo_bob1.functions import *

@instrument
def limited_results(spark: SparkSession, total_sales_desc: DataFrame) -> DataFrame:
    return total_sales_desc.limit(25)
