from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dataquality.config.ConfigStore import *
from dataquality.functions import *

def by_sales_total_desc(spark: SparkSession, aggregate_customer_sales: DataFrame) -> DataFrame:
    return aggregate_customer_sales.orderBy(col("sales_total").desc())
