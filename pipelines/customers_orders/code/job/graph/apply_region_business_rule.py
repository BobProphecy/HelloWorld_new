from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

@instrument
def apply_region_business_rule(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return add_rule(in0, Region_Bus_Rule())
