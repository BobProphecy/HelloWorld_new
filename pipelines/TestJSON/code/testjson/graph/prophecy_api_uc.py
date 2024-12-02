from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def prophecy_api_uc(spark: SparkSession, flatten_api_schema: DataFrame):
    flatten_api_schema.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`bobwelshmer`.`demo_output`.`prophecy_api_uc`")
