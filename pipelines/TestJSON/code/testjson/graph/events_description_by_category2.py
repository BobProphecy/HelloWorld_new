from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def events_description_by_category2(spark: SparkSession, flatten_schema: DataFrame) -> DataFrame:
    df1 = flatten_schema.groupBy(col("result_events_category2"))

    return df1.agg(collect_list(col("result_events_description")).alias("Events_Desc"))
