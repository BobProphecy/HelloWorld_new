from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs import *

def CalcCases(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        (col("has_fm") & col("is_high_income")).alias("has_fm_high_income"), 
        (col("has_fm") & (~ col("is_high_income"))).alias("has_fm_low_income"), 
        ((~ col("has_fm")) & col("is_high_income")).alias("no_fm_high_income"), 
        ((~ col("has_fm")) & (~ col("is_high_income"))).alias("no_fm_low_income"), 
        col("zip"), 
        col("num_farmers_markets"), 
        col("high_income_percent"), 
        col("zipcode"), 
        col("high_income_returns"), 
        col("low_income_returns"), 
        col("all_returns"), 
        col("is_high_income"), 
        col("has_fm")
    )
