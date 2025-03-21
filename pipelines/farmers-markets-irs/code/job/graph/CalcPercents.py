from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

def CalcPercents(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        ((lit(100) * col("has_fm_high_income")) / col("has_fm")).alias("has_fm_high_income_percent"), 
        ((lit(100) * col("no_fm_high_income")) / col("no_fm")).alias("no_fm_high_income_percent"), 
        col("has_fm_high_income"), 
        col("has_fm_low_income"), 
        col("no_fm_high_income"), 
        col("no_fm_low_income"), 
        col("num_zipcodes")
    )
