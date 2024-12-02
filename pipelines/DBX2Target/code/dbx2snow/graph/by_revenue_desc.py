from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dbx2snow.config.ConfigStore import *
from dbx2snow.udfs import *

def by_revenue_desc(spark: SparkSession, revenue_by_customer: DataFrame) -> DataFrame:
    return revenue_by_customer.orderBy(col("REVENUE").desc())
