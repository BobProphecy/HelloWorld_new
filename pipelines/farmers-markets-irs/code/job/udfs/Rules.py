from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *

@execute_rule
def Region_Bus_Rule(country_code: Column=lambda: col("country_code")):
    return when((country_code == lit("US")), lit("North America"))\
        .when((country_code == lit("CA")), lit("North America"))\
        .when((country_code == lit("MX")), lit("North America"))\
        .when((country_code == lit("BR")), lit("South America"))\
        .when((country_code == lit("IN")), lit("Asia"))\
        .otherwise(lit("Other"))\
        .alias("region")
