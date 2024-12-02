from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testjson.config.ConfigStore import *
from testjson.udfs import *

def flatten_schema(spark: SparkSession, old_events_JSON: DataFrame) -> DataFrame:
    flt_col = old_events_JSON.withColumn("result_events", explode_outer("result.events")).columns
    selectCols = [col("result_count") if "result_count" in flt_col else col("result.count").alias("result_count"),                   col("result_events_category1") if "result_events_category1" in flt_col else col("result_events.category1")\
                    .alias("result_events_category1"),                   col("result_events_category2") if "result_events_category2" in flt_col else col("result_events.category2")\
                    .alias("result_events_category2"),                   col("result_events_date") if "result_events_date" in flt_col else col("result_events.date")\
                    .alias("result_events_date"),                   col("result_events_description") if "result_events_description" in flt_col else col("result_events.description")\
                    .alias("result_events_description"),                   col("result_events_granularity") if "result_events_granularity" in flt_col else col("result_events.granularity")\
                    .alias("result_events_granularity"),                   col("result_events_lang") if "result_events_lang" in flt_col else col("result_events.lang")\
                    .alias("result_events_lang")]

    return old_events_JSON.withColumn("result_events", explode_outer("result.events")).select(*selectCols)
