from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from dbx2snow.config.ConfigStore import *
from dbx2snow.udfs import *

def limit_50(spark: SparkSession, by_revenue_desc: DataFrame) -> DataFrame:
    return by_revenue_desc.limit(50)
