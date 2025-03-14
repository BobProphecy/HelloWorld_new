from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def distinct_customer_ids(spark: SparkSession, select_customer_id: DataFrame) -> DataFrame:
    return select_customer_id.distinct()
